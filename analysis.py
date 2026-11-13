class ScatterPlotter:
    def init(self, x, y):
        self.x = x
        self.y = y
        plt.figure(figsize=(8, 5))
        
    def plot(self, color='blue', size=50):
        plt.scatter(self.x, self.y, c=color, s=size, alpha=0.7)
        
    def add_labels(self, xlabel, ylabel, title):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(True)
        plt.show()

# مثال استفاده:
# plotter = ScatterPlotter([1, 2, 3, 4], [10, 20, 25, 30])
# plotter.plot(color='purple', size=100)
# plotter.add_labels('X Values', 'Y Values', 'Scatter Plot Example')