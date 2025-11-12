# This is "Task A" - a complex new feature.
# This file imports from 'topic6_task_A_utils.py'.
# A full "context" will involve having BOTH files open.

from topic6_task_A_utils import load_data_from_source


class DataAnalyticsReport:
    """
    A class representing the new, complex analytics feature
    that you are working on.
    """

    def __init__(self):
        print("Initializing complex data report...")
        self.raw_data = None
        self.processed_data = None

    def load_data(self, source_id: str):
        """
Section 1: Data Ingestion
        """
        print(f"Loading data from source {source_id}...")
        # The presenter will add a BOOKMARK on the line below
        self.raw_data = load_data_from_source(source_id)
        print("Data loaded.")

    def process_data(self):
        """
Section 2: Data Processing (The part you are working on)
        """
        if self.raw_data is None:
            print("No data to process.")
            return

        print("Processing raw data...")
        temp_data = [row * 1.05 for row in self.raw_data]  # Simulate some logic

        # The presenter will add a BREAKPOINT on the line below
        self.processed_data = sum(temp_data)


        print(f"Data processed. Final value: {self.processed_data}")
        return self.processed_data

    def __repr__(self):
        return f"Report(Data={self.processed_data})"


if __name__ == "__main__":
    report = DataAnalyticsReport()
    report.load_data("source-123")
    report.process_data()
