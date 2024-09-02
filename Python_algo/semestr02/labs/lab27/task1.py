"""
Реализуете программу, которая нарисует на холсте
рисунок светофора (использовать различные фигуры, стили, цвета)
"""

from tkinter import Tk, Canvas, Frame, BOTH


class TrafficLight(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.master.title("Светофор")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        # корпус светофора
        canvas.create_rectangle(70, 20, 130, 180, outline="black", fill="gray")
        # красный сигнал
        canvas.create_oval(80, 30, 120, 70, outline="black", fill="red")
        # жёлтый сигнал
        canvas.create_oval(80, 80, 120, 120, outline="black", fill="yellow")
        # зелёный сигнал
        canvas.create_oval(80, 130, 120, 170, outline="black", fill="green")

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = TrafficLight(root)
    root.geometry("200x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()



