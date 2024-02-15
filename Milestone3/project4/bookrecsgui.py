from cgitb import text
from breezypythongui import EasyFrame
from bookrecs import friends, recommend, report

class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title='Book Recomendations', background='#B09A6D')
        self.addButton(text='Friends', row=0, column=0, command=self.handleButtonClick_Friends)
        self.addButton(text='Recomendations', row=0, column=1, command=self.handleButtonClick_Recomendations)
        self.addButton(text='Report', row=0, column=2, command=self.handleButtonClick_Report)

    def handleButtonClick_Friends(self):
        name = self.prompterBox(title='Friends', promptString='Input Reader Name:')
        friends1 = friends(name)
        if friends1 != 'no':
            self.messageBox(title= f'Friends of {name}', message=('\n'.join(friends1)), width= 15,)
        else:
            self.messageBox(title= 'Error', message=f'Reader {name} not found.')
    def handleButtonClick_Recomendations(self):
        name = self.prompterBox(title='Recommendations', promptString='Input Reader Name:')
        friends1 = friends(name)
        recs = recommend(name)
        recslst = []
        for i in recs:
            recslst.append(i[0]+', '+i[1])
        if recs != 'no':
            self.messageBox(title= f'Recommendations for {name}', message=(f'Recommendations for {name} from {friends1[0]} and {friends1[1]}:\n\t'+'\n\t'.join(recslst)), width= 75, height= 15)
        else:
            self.messageBox(title= 'Error', message=f'Reader {name} not found.')
    def handleButtonClick_Report(self):
        recslst = report()
        self.messageBox(title = 'Report', message=recslst, width=75, height=35)


def main():
    BookRecsGui().mainloop()

if __name__ == '__main__':
    main()