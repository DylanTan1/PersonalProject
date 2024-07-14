import numpy as np
import os
from PIL import Image, ImageSequence

class video_augmenter:
    
    #Loads the video and returns an array of images
    #DO NOT RUN THIS MANUALLY. IT WILL BE RUN BY VIDEO AUGMENT METHODS
    def load_video(self, path, modality = "RGB"):
        frames = []
        with open(path, 'rb') as f:
            with Image.open(f) as video:
                index = 1
                for frame in ImageSequence.Iterator(video):
                    frames.append(frame.convert(modality))
                    index +=1
        return frames
    
    #Video augment method
    #FLips the video horizontally
    def horizontal_flip(self, path):
        frames = self.load_video(path)
        
        if isinstance(frames[0],np.ndarray):
            return [np.fliplr(img) for img in frames]
        elif isinstance(frames[0], Image.Image):
            return [img.transpose(Image.FLIP_LEFT_RIGHT) for img in frames]
        else:
            raise TypeError('Expected numpy.ndarray or PIL.Image' +
                            ' but got list of {0}'.format(type(frames[0])))
    
    #Video augment method
    #FLips the video vertically 
    def vertical_flip(self, path):
        frames = self.load_video(path)
        
        if isinstance(frames[0], np.ndarray):
            return [np.flipud(img) for img in frames]
        elif isinstance(frames[0], Image.Image):
            return [img.transpose(Image.FLIP_TOP_BOTTOM) for img in frames]
        else:
            raise TypeError('Expected numpy.ndarray or PIL.Image' +
                            ' but got list of {0}'.format(type(frames[0])))
    
    
    #Performs the video augmentation
    #Checks original video folder and augmented video folder
    #Performs all video augmentation and save into folder
    def perform_augmentation(self,folder_name):
        if not os.path.isdir(folder_name):
            raise Exception("Folder does not exist")
        
        path = 'augmented_video'
        if not os.path.isdir(path):
            os.makedirs(path)
        
        for file_name in os.listdir(folder_name):
            original = folder_name + '/' + file_name
            hori_flipped = self.horizontal_flip(original)
            vert_flip = self.vertical_flip(original)
            hori_flipped[0].save(path + '/' + 'hori_flip.gif', save_all=True, append_images=hori_flipped[1:], duration=35, loop=0)
            vert_flip[0].save(path + '/' + 'vert_flip.gif', save_all=True, append_images=vert_flip[1:], duration=35, loop=0)
            
    
if __name__ == '__main__':
    test = video_augmenter()
    test.perform_augmentation('videos')