import plotly.express
import pandas

df = pandas.read_csv('stock2.csv')
print(df)

figure = plotly.express.line(df, x='Date', y='Price')
figure.show()