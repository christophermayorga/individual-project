Abstract: Using data from the U.S. News and World Report on over 700 colleges and universities, I created a linear regression model that predicts
graduation rate based on selected features. My goal was to provide prospective college students insight on what statistics they should focus on when selecting their school. In exploratory analysis, I found five key drivers that were used to predict graduation rate: out-of-state tuition, number of new students enrolled, public or private, student/faculty ratio, and acceptance rate. In modeling, I set the baseline prediction to the mean graduation rate, which resulted in a root mean squared error of 17.14. I chose ordinary least squares linear regression to predict graduation rates, which had a root mean squared error of 14.49. This project contributes to research aimed at assisting high school guidance counselors, college advisors, and aspiring students.

### U.S. News and World Report's College Data

**Description**

Statistics for a large number of US Colleges from the 1995 issue of US News and World Report.

**Format**

A data frame with 777 observations on the following 18 variables.

`Private`
A factor with levels No and Yes indicating private or public university

`Apps`
Number of applications received

`Accept`
Number of applications accepted

`Enroll`
Number of new students enrolled

`Top10perc`
Pct. new students from top 10% of H.S. class

`Top25perc`
Pct. new students from top 25% of H.S. class

`F.Undergrad`
Number of fulltime undergraduates

`P.Undergrad`
Number of parttime undergraduates

`Outstate`
Out-of-state tuition

`Room.Board`
Room and board costs

`Books`
Estimated book costs

`Personal`
Estimated personal spending

`PhD`
Pct. of faculty with Ph.D.'s

`Terminal`
Pct. of faculty with terminal degree

`S.F.Ratio`
Student/faculty ratio

`perc.alumni`
Pct. alumni who donate

`Expend`
Instructional expenditure per student

`Grad.Rate`
Graduation rate

**Source**

This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University. The dataset was used in the ASA Statistical Graphics Section's 1995 Data Analysis Exposition.

**References**

James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) An Introduction to Statistical Learning with applications in R, www.StatLearning.com, Springer-Verlag, New York