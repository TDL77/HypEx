# HypEx: Advanced Causal Inference and AB Testing Toolkit

[![Telegram](https://img.shields.io/badge/chat-on%20Telegram-2ba2d9.svg)](https://t.me/hypexchat)
![Last release](https://img.shields.io/badge/pypi-v0.1.1-darkgreen)
![Python versions](https://img.shields.io/badge/python-3.8_|_3.9_|_3.10_|_3.11_|_3.12-blue)
![Pypi downloads](https://img.shields.io/badge/downloads-5K-1E782B)

## Introduction

HypEx (Hypotheses and Experiments) is a comprehensive library crafted to streamline the causal inference and AB testing
processes in data analytics. Developed for efficiency and effectiveness, HypEx employs Rubin's Causal Model (RCM) for
matching closely related pairs, ensuring equitable group comparisons when estimating treatment effects.

Boasting a fully automated pipeline, HypEx adeptly calculates the Average Treatment Effect (ATE), Average Treatment
Effect on the Treated (ATT), and Average Treatment Effect on the Control (ATC). It offers a standardized interface for
executing these estimations, providing insights into the impact of interventions across various population subgroups.

Beyond causal inference, HypEx is equipped with robust AB testing tools, including Difference-in-Differences (
Diff-in-Diff) and CUPED methods, to rigorously test hypotheses and validate experimental results.

## Features

- **Faiss KNN Matching**: Utilizes Faiss for efficient and precise nearest neighbor searches, aligning with RCM for
  optimal pair matching.
- **Data Filters**: Built-in outlier and Spearman filters ensure data quality for matching.
- **Result Validation**: Offers multiple validation methods, including random treatment, feature, and subset
  validations.
- **Data Tests**: Incorporates SMD, KS, PSI, and Repeats tests to affirm the robustness of effect estimations.
- **Feature Selection**: Employs LGBM and Catboost feature selection to pinpoint the most impactful features for causal
  analysis.
- **AB Testing Suite**: Features a suite of AB testing tools for comprehensive hypothesis evaluation.
- **Stratification support**: Stratify groups for nuanced analysis
- **Weights support**:  Empower your analysis by assigning custom weights to features, enhancing the matching precision
  to suit your specific research needs

## Warnings

Some functions in HypEx can facilitate solving specific auxiliary tasks but cannot automate decisions on experiment
design. Below, we will discuss features that are implemented in HypEx but do not automate the design of experiments.

### Feature Selection

**Feature selection** models the significance of features for the accuracy of target approximation. However, it does not
rule out the possibility of overlooked features, the complex impact of features on target description, or the
significance of features from a business logic perspective. The algorithm will not function correctly if there are data
leaks.

Points to consider when selecting features:

* Data leaks - these should not be present.
* Influence on treatment distribution - features should not affect the treatment distribution.
* The target should be describable by features.
* All features significantly affecting the target should be included.
* The business rationale of features.
* The feature selection function can be useful for addressing these tasks, but it does not solve them nor does it
  absolve the user of the responsibility for their selection, nor does it justify it.

[Link to ReadTheDocs](https://hypex.readthedocs.io/en/latest/pages/modules/selectors.html#selector-classes)

### Random Treatment

**Random Treatment** algorithm randomly shuffles the actual treatment. It is expected that the treatment's effect on the
target will be close to 0.

These method is not sufficiently accurate marker of a successful experiment.

[Link to ReadTheDocs](https://hypex.readthedocs.io/en/latest/pages/modules/utils.html#validators)

## Installation

```bash
pip install hypex
```

## Quick start

Explore usage examples and tutorials [here](https://github.com/sb-ai-lab/Hypex/blob/master/examples/tutorials/).

### Matching example

```python
from hypex import Matcher
from hypex.utils.tutorial_data_creation import create_test_data

# Define your data and parameters
df = create_test_data(rs=42, na_step=45, nan_cols=['age', 'gender'])

info_col = ['user_id']
outcome = 'post_spends'
treatment = 'treat'
model = Matcher(input_data=df, outcome=outcome, treatment=treatment, info_col=info_col)
results, quality_results, df_matched = model.estimate()
```

### AA-test example

```python
from hypex import AATest
from hypex.utils.tutorial_data_creation import create_test_data

data = create_test_data(rs=52, na_step=10, nan_cols=['age', 'gender'])

info_cols = ['user_id', 'signup_month']
target = ['post_spends', 'pre_spends']

experiment = AATest(info_cols=info_cols, target_fields=target)
results = experiment.process(data, iterations=1000)
results.keys()
```

### AB-test example

```python
from hypex import ABTest
from hypex.utils.tutorial_data_creation import create_test_data

data = create_test_data(rs=52, na_step=10, nan_cols=['age', 'gender'])

model = ABTest()
results = model.execute(
    data=data,
    target_field='post_spends',
    target_field_before='pre_spends',
    group_field='group'
)

model.show_beautiful_result()
```

## Documentation

For more detailed information about the library and its features, visit
our [documentation on ReadTheDocs](https://hypex.readthedocs.io/en/latest/).

You'll find comprehensive guides and tutorials that will help you get started with HypEx, as well as detailed API
documentation for advanced use cases.

## Contributions

Join our vibrant community! For guidelines on contributing, reporting issues, or seeking support, please refer to
our [Contributing Guidelines](https://github.com/sb-ai-lab/Hypex/blob/master/.github/CONTRIBUTING.md).

## More Information & Resources

[Habr (ru)](https://habr.com/ru/companies/sberbank/articles/778774/) - discover how HypEx is revolutionizing causal
inference in various fields.      
[A/B testing seminar](https://www.youtube.com/watch?v=B9BE_yk8CjA&t=53s&ab_channel=NoML) - Seminar in NoML about
matching and A/B testing       
[Matching with HypEx: Simple Guide](https://www.kaggle.com/code/kseniavasilieva/matching-with-hypex-simple-guide) -
Simple matching guide with explanation           
[Matching with HypEx: Grouping](https://www.kaggle.com/code/kseniavasilieva/matching-with-hypex-grouping) - Matching
with grouping guide    
[HypEx vs Causal Inference and DoWhy](https://www.kaggle.com/code/kseniavasilieva/hypex-vs-causal-inference-and-dowhy) -
discover why HypEx is the best solution for causal inference           
[HypEx vs Causal Inference and DoWhy: part 2](https://www.kaggle.com/code/kseniavasilieva/hypex-vs-causal-inference-part-2) -
discover why HypEx is the best solution for causal inference

### Testing different libraries for the speed of matching

Visit [this](https://www.kaggle.com/code/kseniavasilieva/hypex-vs-causal-inference-part-2) notebook ain Kaggle and
estimate results by yourself.

| Group size             | 32 768   | 65 536     | 131 072   | 262 144   | 524 288    | 1 048 576   | 2 097 152    | 4 194 304     |
|------------------------|---------|-----------|----------|----------|-----------|-----------|------------|-------------|
| Causal Inference       | 46s | 169s | None     | None     | None      | None      | None       | None        |
| DoWhy                  | 9s | 19s  | 40s | 77s | 159s | 312s | 615s  | 1 235s  |
| HypEx with grouping    | 2s | 6s   | 16s | 42s | 167s | 509s | 1 932s | 7 248s  |
| HypEx without grouping | 2s  | 7s   | 21s | 101s | 273s | 982s | 3 750s | 14 720s |

## Join Our Community

Have questions or want to discuss HypEx? Join our [Telegram chat](https://t.me/HypExChat) and connect with the community
and the developers.

## Conclusion

HypEx stands as an indispensable resource for data analysts and researchers delving into causal inference and AB
testing. With its automated capabilities, sophisticated matching techniques, and thorough validation procedures, HypEx
is poised to unravel causal relationships in complex datasets with unprecedented speed and precision.

##                                                                              
