#creando graficas con el paquete matplotlib
import matplotlib.pyplot as plt

def generate_bar_chart():
    
    labels = ["a", "b", "c"]
    values = [100,150,90]
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()
if __name__ == "__main__":
    generate_bar_chart()


