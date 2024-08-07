# Redefine pandas and retry creating and saving the CSV file
import pandas as pd

# Part 1 of data (redefinition)
data1 = [
    ["Which type of filter is most effective in removing 'salt-and-pepper' noise?", 
     "A. Gaussian filter", 
     "B. Median filter", 
     "C. Low-pass filter", 
     "D. High-pass filter", 
     "", "B"],

    ["What is the primary effect of applying a low-pass filter to an image?", 
     "A. Sharpening", 
     "B. Blurring", 
     "C. Enhancing edges", 
     "D. Reducing noise", 
     "", "B"],

    ["Which filter is used to enhance edges in an image?", 
     "A. Low-pass filter", 
     "B. High-pass filter", 
     "C. Band-pass filter", 
     "D. Median filter", 
     "", "B"],

    ["What does a high-pass filter do to low-frequency components?", 
     "A. Enhances them", 
     "B. Attenuates them", 
     "C. Removes them completely", 
     "D. Leaves them unchanged", 
     "", "B"],

    ["Which filtering technique is best for removing periodic noise?", 
     "A. Gaussian filter", 
     "B. Median filter", 
     "C. Notch filter", 
     "D. High-pass filter", 
     "", "C"],

    ["What is the main purpose of using a Gaussian filter in image processing?", 
     "A. Edge detection", 
     "B. Smoothing", 
     "C. Noise reduction", 
     "D. Sharpening", 
     "", "B"],

    ["Which filter type is commonly used for image sharpening?", 
     "A. Low-pass filter", 
     "B. High-pass filter", 
     "C. Band-stop filter", 
     "D. Median filter", 
     "", "B"],

    ["How does a median filter handle the pixels in an image?", 
     "A. Averages pixel values", 
     "B. Multiplies pixel values", 
     "C. Replaces pixel values with the median of neighboring pixels", 
     "D. Replaces pixel values with the maximum of neighboring pixels", 
     "", "C"],

    ["What effect does a band-pass filter have on an image?", 
     "A. Removes both high and low frequencies", 
     "B. Enhances high frequencies", 
     "C. Enhances low frequencies", 
     "D. Allows a specific range of frequencies to pass", 
     "", "D"],

    ["Which of the following filters is most effective at reducing Gaussian noise?", 
     "A. High-pass filter", 
     "B. Low-pass filter", 
     "C. Notch filter", 
     "D. Band-stop filter", 
     "", "B"]
]

# Create a DataFrame for Part 1
df1 = pd.DataFrame(data1, columns=[
    "Question", "Option A", "Option B", "Option C", "Option D", "Option E", "Correct Answer"
])

# Save the DataFrame for Part 1 to a CSV file
csv_file_path1 = 'questions_and_answers_part1.csv'
df1.to_csv(csv_file_path1, index=False, sep=';')

csv_file_path1
