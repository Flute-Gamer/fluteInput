


def drawFunc(volume, color):

    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        x_vals.append(next(index))
        y_vals.append(volume)

        plt.cla()
        plt.plot(x_vals, y_vals)

    ani = FuncAnimation(plt.gcf(), animate, interval=200)

    plt.tight_layout()
    plt.show()
        
    return