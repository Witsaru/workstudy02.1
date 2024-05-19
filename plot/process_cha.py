import matplotlib.pyplot as plt
import csv
import pandas

class plotprocesscha():
    def __init__(self) -> None:
        self.axis_y = 13
        self.axis_x_text = -5
        # "Operation", "Inspection", "Transport", "Delay", "Storage"
        self.symbol_data = {
            "Operation": 0,
            "Transport": 0.5,
            "Delay": 1,
            "Inspection": 1.5,
            "Storage":2
        }

        self.fig, self.ax = plt.subplots(figsize=(10, 6))

        self.data = {}
        self.data_n = {}
    
    def text_process(self,x, y,process):
        self.ax.text(x, y, process)

    def plot_process_chart(self,ax, x, y):
    
        ax.scatter(x, y, s=50, marker='o', color='black')

    def plot_process_chart_main(self):
        self.ax.scatter(0, 15, s=500, marker='o', color='darkblue')
        self.ax.scatter(0.5, 15, s=500, marker='>', color='darkblue')
        self.ax.scatter(1, 15, s=500, marker='H', color='darkblue')
        self.ax.scatter(1.5, 15, s=500, marker= 's', color='darkblue')
        self.ax.scatter(2, 15, s=500, marker='v', color='darkblue')

    def plot_procha(self,df):
        try:
            self.plot_process_chart_main()
            for index, row in df.iterrows():
                proli = row["Data"]
                opli = self.symbol_data[row["Operation"]]
                self.data[proli] = opli

            for step,symbol in self.data.items():
                self.plot_process_chart(self.ax, symbol, self.axis_y)
                self.text_process(self.axis_x_text, self.axis_y, step)
                self.data_n[step] = (symbol,self.axis_y)
                self.axis_y -= 1

            for i in range(len(self.data) - 1):
                # print(f'x:{steps[list(steps.keys())[i]][0]}, y:{steps[list(steps.keys())[i + 1]][0]}')
                self.ax.plot([self.data_n[list(self.data_n.keys())[i]][0], self.data_n[list(self.data_n.keys())[i + 1]][0]],
                        [self.data_n[list(self.data_n.keys())[i]][1], self.data_n[list(self.data_n.keys())[i + 1]][1]], 'k-', lw=1)


            self.ax.set_xlim(-1, 3)
            self.ax.set_ylim(0, max([pos[1] for pos in self.data_n.values()]) + 3)
            self.ax.axis('off')
            # print(self.data)

            # แสดงแผนภาพ Two-handed Process Chart
            plt.show()

        except Exception as e:
            print("Error:", e)