
import zarr
class DataSaver():
    '''Saveing a matrix in a zarr chunk, filling up to targetsize using np.nan'''

    def __init__(self,savefile,sample_size,target_shape,chunk_len):
        self.savefile = savefile
        self.sample_size = sample_size
        self.shape = target_shape
        self.chunk_len = chunk_len

        self.matrix = np.empty(self.shape)
        self.savefile = zarr.open(self.savefile , mode = 'w', shape= (self.shape[0],self.shape[1],self.sample_size*self.chunk_len),chunks = (self.shape[0],self.shape[1],self.chunk_len))

    def save(self,inp_matrix,idx):

        self.preproc(inp_matrix)
        self.savefile[:,:,idx] = self.matrix

    def preproc(self,inp_matrix):

        self.matrix.fill(np.nan)
        self.matrix[:inp_matrix.shape[0],:inp_matrix.shape[1]] = inp_matrix 
