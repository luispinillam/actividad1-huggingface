from datasets import load_dataset
import pandas as pd


class HFDatasetLoader:
    def __init__(self, dataset_id, split="train"):
        self.dataset_id = dataset_id
        self.split = split

    def obtener_dataframe(self):
        dataset = load_dataset(
            self.dataset_id,
            split=self.split
        )

        df = dataset.to_pandas()

        return df