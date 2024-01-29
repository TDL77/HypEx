"""Feature selection class using LAMA."""
import logging
from typing import List

import pandas as pd

logger = logging.getLogger("lama_feature_selector")
console_out = logging.StreamHandler()
logging.basicConfig(
    handlers=(console_out,),
    format="[%(asctime)s | %(name)s | %(levelname)s]: %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    level=logging.INFO,
)


class FeatureSelector:
    """Class of LAMA Feature selector. Select top features. By default, use LGM.
    # TODO: write some feature selector"""

    def __init__(
            self,
            outcome: str,
            treatment: str,
            feature_selection_method,
    ):
        """Initialize the LamaFeatureSelector.

        Args:
            outcome:
                The target column
            treatment:
                The column that determines control and test groups
            use_algos:
                List of names of LAMA algorithms for feature selection
        """
        self.outcome = outcome
        self.treatment = treatment
        self.feature_selection_method = feature_selection_method

    def perform_selection(self, df: pd.DataFrame) -> pd.DataFrame:
        """Trains a model and returns feature scores.

        This method defines metrics, applies the model, creates a report, and returns feature scores

        Args:
            df:
                Input data

        Returns:
            A DataFrame containing the feature scores from the model

        """
        roles = {
            "target": self.outcome,
            "drop": [self.treatment],
        }
        report_df = self.feature_selection_method(
            df=df,
            info_col_list=None,
            target=self.outcome,
            treatment_col=self.treatment,
            weights_col_list=None,
            category_col_list=None,
        )
        return report_df
