# Data visualizations are how we communicate data. We don’t read the numbers off a spreadsheet or list every number in a trend to communicate a point – we make a visualization to show them.

# There’s often more than one possible chart we can use for a dataset. But different charts emphasize different questions, arguments, or relationships in the data, and whichever we choose should help translate that data relationship into a visual relationship.

# One big consideration when choosing a chart type is how many variables we’re comparing. Univariate charts help us visualize a change in one variable.

# The classic bivariate example is the scatter plot — one variable on the x-axis, another on the y-axis, and each point helps us compare the two variables by its position on the graph.
# Because we’re relying on the idea that each variable increases as we move up the X or Y axis, the scatterplot only makes sense for numeric variables, not categorical.

# A line chart is another common bivariate chart, often measuring a variable changing over time. A stock chart, for example, measures the value of a company over time.
# A line chart with multiple lines for different variables is a multivariate chart.

# We’ll dive deeper into accessibility later, but for now note that information redundancy is also an important practice to ensure that colorblind viewers can access all the information in a chart. To sum up, information redundancy visualizes the same information using multiple different aesthetic properties. It’s important for readability, organization and prioritization of information, and accessibility.

# The most commonly discussed accessibility concern is color, since color blindness affects 1 in 12 males and 1 in 200 females. That’s more common than we tend to think! There are a few different types of color blindness: check out the images for simulations of each form.

# The big takeaway when designing for color accessibility is to think not only about the hue of a color (e.g. red, green, or purple), but the value as well (e.g. bright red, light green, dark purple). Good color comparisons use high contrast values, not just different hues.
# It’s also important to use readable fonts in readable sizes, and make sure they’re web-accessible if online.

# Finally, for online data visualizations, make sure to include alt text as we would for any other web image. Alt text ensures that users experiencing a visualization through a screen reader won’t miss out on whatever information it contains.


# To recap, here’s a checklist for baseline accessibility:

# Colorblind-friendly color palettes
# Large enough font size
# Readable, web-accessible font type
# Alt text on data visualization images online



# We can apply it when it comes to…

# Readability: keep the reading level to a high school level whenever possible
# Prior knowledge: define unfamiliar terms and avoid unnecessary jargon
# Information overload: introduce new information with intentional pacing and organization


# for most audiences, and especially for broad or unknown audiences, keeping accessibility in mind will help everyone get the most out of our visualizations.

# Data does not speak for itself, and often, the author of a data viz is the person in the best position to create insightful, helpful annotations.



# While the best graphs really do teach us something new, and help us understand a deeper truth using data, graphs can also be misleading, both intentionally or unintentionally. We shouldn’t ever assume that a data visualization shows us the truth, the whole truth, and nothing but the truth.


# If you’re making the graph, instead of using a big break…

# Keep enough context to view differences in proportion to a meaningful amount, OR
# Make two graphs, one without a break and one “zoomed in”, OR
# Choose a visualization type that shows the change, rather than the raw numbers


# Almost all graphs use a linear scale, where the numbers count up by a consistent interval – tenths of a centimeter or millions of dollars, if it’s the same interval, it’s a linear scale.

# The other scaling option is a logarithmic scale, a.k.a. log scale. The log scale is common for showing exponential growth that won’t fit on the page with a linear scale, but it’s almost never a good choice for a general audience. Unless people use log scales regularly, they tend to have trouble interpreting them correctly.

# Last thing about axes and scaling: generally, we measure time horizontally, putting that variable on the x-axis. For the vast majority of circumstances, this makes the most sense and helps readers to intuit what the graph measures.

# First up, we tend to view darker colors as “more” and lighter colors as “less.” For example, if we’re visualizing which US states have the most pet ferrets, California – with the most pet ferrets of any state – should be the darkest state on the map. When this scale is reversed, people will tend to just read the graph wrong rather than reading the legend carefully.

# A good title is one of the best and fastest tools for making a more understandable visualization. Lots of confusion can be saved with a descriptive title.

# Like a good title, annotations on a graph also help the viewer to understand what’s going on. Annotations are perfect for calling out points of interest, explaining outliers, or including background information that a viewer won’t necessarily know from just looking at the graph.