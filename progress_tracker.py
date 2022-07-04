#===============================================================================================
# Keeping track of progress in a for loop made easy!'
# Date: 11.05.2022
# Author: Tobias Fritz
#===============================================================================================

class Progress():
    ''' Keeping track of progress in a for loop made easy!'''

    def __init__(self,Iterable):
        self.complete = len(Iterable)
        self.progress_nom = 0
        self.progress_percent = 0
        print(f'Calculation: {self.progress_percent}% complete!',  end='\r', flush=True)
    
    def Update(self):

        # Update Progress every time it is called
        self.progress_nom += 1
        self.progress_percent= round(self.progress_nom/self.complete * 100)
    
    def Show(self,criterion=5):

        # Print progress in the % intervals given by the criterion option (default: every 5% increment)
        if self.progress_percent == 0 :
            print(f'Calculation: {self.progress_percent}% complete!',  end='\r', flush=True)
        if self.progress_percent % criterion == 0 and self.progress_percent != 100 :
            print(f'Calculation: {self.progress_percent}% complete!',  end='\r', flush=True) 
        elif self.progress_percent == 100:
            print(f'Calculation complete!      ',  end='\r', flush=True) 
