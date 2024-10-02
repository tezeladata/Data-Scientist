import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns


np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

# pts 10
knicks_pts_10 = nba_2010.pts[nba_2010.fran_id == "Knicks"]
nets_pts_10 = nba_2010.pts[nba_2010.fran_id == "Nets"]

# Mean 10
mean_knicks = knicks_pts_10.mean()
mean_nets = nets_pts_10.mean()
diff_means_2010 = mean_knicks - mean_nets
print(diff_means_2010)

# Histogram 10
plt.hist(knicks_pts_10, color="blue", label="Knicks points", density=True, alpha=0.5)
plt.hist(nets_pts_10, color="red", label="Nets points", density=True, alpha=0.5)
plt.legend()
plt.show()
plt.close()



# pts 14
knicks_pts_14 = nba_2014.pts[nba_2014.fran_id == "Knicks"]
nets_pts_14 = nba_2014.pts[nba_2014.fran_id == "Nets"]

# Mean 14
mean_knicks = knicks_pts_14.mean()
mean_nets = nets_pts_14.mean()
diff_means_2014 = mean_knicks - mean_nets
print(diff_means_2014)

# Histogram 14
plt.hist(knicks_pts_14, color="green", label="Knicks points",density=True, alpha=0.5)
plt.hist(nets_pts_14, color="yellow", label="Nets points", density=True, alpha=0.5)
plt.legend()
plt.show()
plt.close()



# Boxplots for 2010 teams points
sns.boxplot(data=nba_2010, x="fran_id", y="pts")
plt.show()
plt.close()


# Correlation between two categorical variables
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_freq)

# Proportions:
location_result_proportions = location_result_freq / len(nba_2010)
print(location_result_proportions)

# Chi-square statistic
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)



# Covariance
point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)

# Correlation
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

# Scatter to show correlation:
plt.scatter(x=nba_2010.forecast, y=nba_2010.point_diff)
plt.xlabel("Forecast")
plt.ylabel("Point diff")
plt.show()
plt.close()