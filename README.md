# Likert-Clusters v1.0 for Finnish parliamentary election data 2015
## A notebook for cluster analysis and visualization of survey data in likert scale

This notebook applies K-means algorithm for likert data (questionaries with answers betwen 1 to 5) and provides functions to visualize the emerging clusters in various ways.

Finland's parliamentary election data from 2015 is used as an example, but this notebook is designed to be easily used with another dataset.

### About cluster analysis

The assumption this notebook makes is that if you get a bunch of answers then most of your participants tend to respond in ways that fall into several similar groupings (clusters), and this alone tells you something about the target population's conceptions regarding your questions.

There are a number of methods designed for visualizing likert data (e.g. item response theory, categorical data analyses, multidimensional nonlinear descriptive analysis, fuzzy probability & statistics, and dissimilarity/similarity analyses which require strong knowledge in statistics). Luckily, by using fairly simple distance measures and cluster algorithms you can compare individual responses for each participant to better understand whether their answers are all over the place or tend to fall into groups (the latter is the preferred result). 

## The notebook

See [likert-clusters notebook on Finland's parliamentery election 2015](https://github.com/tjkemp/likert-clusters/blob/master/likert-clusters.ipynb).


## Example visualizations from Finland parliamentary election 2015 data

For more information see the notebook.

#### Histograms

![Histogram](https://github.com/tjkemp/likert-clusters/blob/master/images/results.png)

#### Parallel coordinates

![Parallel coordinates](https://github.com/tjkemp/likert-clusters/blob/master/images/parallel_coordinates.png)

#### Dimension reduction

![Dimension reduction](https://github.com/tjkemp/likert-clusters/blob/master/images/dimension_reduction.png)

#### Hierarchical clustering

![Hierarchical clustering](https://github.com/tjkemp/likert-clusters/blob/master/images/hierarchical.png)

### Using this notebook with custom data

Your input data should be pre-processed to a csv file of following format, e.g: 

| id | group1    | group2    | question1 | question2 | question3 |
|----|-----------|-----------|-----------|-----------|-----------|
| 1  | 1         | 1         | 3         | 4         | 4         |
| 2  | 1         | 5         | 5         | 5         | 2         |
| 3  | 0         | 7         | 1         | 3         | 4         |

Header row and id column can be arbitrary and do not show in plots but are expected to be included in the data. Question cells should have values between 1-5. Groups are features/clusters created in the preprocess phase and they should be between id and question columns.

To use this notebook:
1. Preprocess your data into suitable format (see data directory for examples).
2. Copy the notebook as a template.
3. Configure the notebook.
  - Configure settings section (the filename, file_delimiter and which column the likert data starts).
  - Set the question names as a list, and if needed any other data such as plain text meanings of groups' values for purposes of showing them in plots.
  - Read group columns as label lists if you want to use them in plots as clusters.
5. Run each cell.

## Licenses

- [MIT LICENSE](LICENSE)
- Data source: https://yle.fi/uutiset/3-7869597 (in finnish) & license: [CC BY-SA 1.0](https://creativecommons.org/licenses/by-sa/1.0/legalcode)
([license in human readable form](https://creativecommons.org/licenses/by-sa/1.0/))

## Author

- [tjkemp](https://github.com/tjkemp)
