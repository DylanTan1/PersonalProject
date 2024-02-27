import numpy as np
from PIl import Image, ImageSequence

class video_augmenter:
    
    def load_video(self, path, modality = "RGB"):
        frames = []
        with open(path, 'rb') as f:
            with Image.open(f) as video:
                index = 1
                for frame in ImageSequence.Iterator(video):
                    frames.append(frame.convert(modality))
                    index +=1
        return frames
    
    def horizontal_flip(self, path):
        frames = self.load_video(path)
        
        if isinstance(frames[0],np.ndarray):
            return [np.fliplr(img) for img in frames]
        elif isinstance(frames[0], Image.Image):
            return [img.transpose(Image.FLIP_LEFT_RIGHT) for img in frames]
        else:
            raise TypeError('Expected numpy.ndarray or PIL.Image' +
                            ' but got list of {0}'.format(type(frames[0])))
            
    def vertical_flip(self, path):
        frames = self.load_video(path)
        
        if isinstance(frames[0], np.ndarray):
            return [np.flipud(img) for img in frames]
        elif isinstance(frames[0], Image.Image):
            return [img.transpose(Image.FLIP_TOP_BOTTOM) for img in frames]
        else:
            raise TypeError('Expected numpy.ndarray or PIL.Image' +
                            ' but got list of {0}'.format(type(frames[0])))