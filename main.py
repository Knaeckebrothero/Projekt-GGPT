"""
Final project
https://github.com/Knaeckebrothero/ISWE

Group 1
Iman Osman 1351664,
Niklas Riel 1253801
"""
import os
import shutil
import sys
import streamlit as st
import matplotlib.pyplot as plt
from io import StringIO
from processing import quickcheck as qs
from processing import reader as rd
from transform.file_contents import FileContents
from database.database import Database
from processing import printer as pr

# Main method of our application
# As far as I understand this is primary convention and there to tell
# other devs that this is a executable script.
if __name__ == '__main__':

    # At the start of the application the downloaded files directory gets
    # cleared
    shutil.rmtree('files/')
    os.makedirs('files/')

    dataset_name = None

    # Static container displaying information regarding the application.
    header_app = st.container()

    with header_app:
        # Title
        st.title('Fix your bad csv')
        st.header('Welcome user, let us fix some poor datafiles...')

    st.header('It´s time to upload your dataset!')

    # Checkbox if the csv contains headers
    headlines = st.checkbox('My dataset has headers')

    # File uploader
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataset_name = uploaded_file.name.lower().replace(".", "_")
        with st.spinner('File is uploading...'):
            # Convert to string:
            stringio = StringIO(uploaded_file.getvalue().decode('utf-8-sig'))
            string_data = stringio.read()

            # Print to file
            path = "files/" + uploaded_file.name
            with open(path, "w", newline='', encoding='utf-8') as f:
                f.write(string_data)
        st.success('File has been successfully uploaded!')

        # Now the file is checked
        with st.spinner('Preprocessing file now...'):
            with open(path) as data:

                # Checks if the file is large enough to justify the effort
                if data.__sizeof__() < 250:

                    # If the file is likely to be of type csv, the
                    # application continues to proceed accordingly
                    if qs.csv_check(data):
                        filename_type = uploaded_file.name.split(".")
                        file = FileContents(
                            filename_type[0], filename_type[1], rd.csv(
                                path, headlines))

                        # Runs etl cleanup
                        file.etl()
        st.success('File has been successfully processed!')

        with st.spinner('Importing file into the database...'):
            # Initiate db and load data into database
            db = Database()
            db.bulkLoad(file)
        st.success('File has been successfully imported into database!')

        # Now the data gets loaded from the database and displayed as a pie chart.
        # This is so that the user can see how large single columns are in
        # comparison
        col1, col2 = st.columns(2)
        col1.header("Proportions")
        col2.header("Remove columns")
        done_remove = False
        continue_printing = False

        df = db.execStatement("SELECT * FROM {}".format(dataset_name))

        done_remove = False
        remove_col = None
        labels = []
        sizes = []
        percent = sys.getsizeof(df) / 100

        for c in df.columns:
            labels.append(c)

        for s in df:
            sizes.append(sys.getsizeof(s) / percent)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax1.axis('equal')

        col1.pyplot(fig1)

        # Now the user gets asked if he would want to remove any columns
        # and is able to print his data into a new file.
        remove_col = col2.text_input(
            "Type in the names of the columns you want to remove, seperated with a -")
        col2.text("If u do not want to remove any just press the button.")
        done_remove = col2.button("Remove & print")

        if done_remove:
            with st.spinner('Printing your file...'):
                try:
                    col = remove_col.split("-")
                    for c in col:
                        df = db.execStatement(
                            "ALTER TABLE {} DROP COLUMN {}".format(
                                dataset_name, c))
                finally:
                    final_ds = db.execStatement(
                        "SELECT * FROM {}".format(dataset_name))
                    pr.csv(final_ds, dataset_name.split("_")[0])
            st.success('File has been printed!')

            # At last the results of our etl pipline are displayed.
            st.text("Here are the results of our etl pipline...")
            st.table(file.changes)

            # The db drops the table as it is no longer needed
            db.execStatement("DROP TABLE {}".format(dataset_name))
