# Likert-Clusters v1.0 for Finnish parliamentary election data 2015
## A notebook for cluster analysis and visualization of survey data in likert scale

The assumption the notebook makes is that if you get a bunch of answers then most of your participants tend to respond in ways that fall into several similar groupings (clusters), and this alone tells you something about the target population's conceptions regarding your questions.

There are a number of methods designed for visualizing likert data (e.g. item response theory, categorical data analyses, multidimensional nonlinear descriptive analysis, fuzzy probability & statistics, and dissimilarity/similarity analyses which require strong knowledge in statistics. Luckily, by using fairly simple distance measures and cluster algorithms you can compare individual responses for each participant to better understand whether their answers are all over the place or tend to fall into groups (the latter is the preferred result). 

This notebook uses to apply K-means algorithm for likert data (questionaries with answers betwen 1 to 5) and then visualize the emerging clusters in various ways. Note: at the moment this notebook only divides the data to two clusters.

### The notebook

See the [likert-clusters notebook on Finland's parliamentery election 2015](https://github.com/tjkemp/likert-clusters/blob/master/likert-clusters.ipynb).


### Example visualizations from Finland parliamentary election 2015 data

For more information see the notebook.

#### Histograms

![Histogram](https://github.com/tjkemp/likert-clusters/blob/master/images/results.png)

#### Parallel coordinates

![Parallel coordinates](https://github.com/tjkemp/likert-clusters/blob/master/images/parallel_coordinates.png)

#### Dimension reduction

![Dimension reduction](https://github.com/tjkemp/likert-clusters/blob/master/images/dimension_reduction.png)

#### Hierarchical clustering

![Hierarchical clustering](https://github.com/tjkemp/likert-clusters/blob/master/images/hierarchical.png)

### Using the notebook for other data

The input data should be a csv-style file, e.g: 

| id | question1 | question2 | question3 | question4 |
|----|-----------|-----------|-----------|-----------|
| 1  | 1         | 2         | 3         | 4         |
| 2  | 5         | 5         | 5         | 5         |
| 3  | 2         | 3         | 1         | 3         |

Header and left-most ids can be arbitrary and do not show in plots but are expected to be included in data. All data cells should have values between 1-5. 

To use the notebook:
1. Clone or download the repo.
2. Preprocess and insert data file into suitable location (e.g. the directory of the notebook).
3. Set filename, file_delimiter, questions and answers into the the notebook.
4. Run each cell.

## Author

- [tjkemp](https://github.com/tjkemp)
