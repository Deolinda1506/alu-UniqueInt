import os
import re
import time

class UniqueInt:
    
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        unique_integers = set()
        
        try:
            with open(inputFilePath, 'r') as file:
                for line in file:
                    integer = UniqueInt.readNextItemFromFile(line)
                    if integer is not None:
                        unique_integers.add(integer)
            
            sorted_integers = sorted(unique_integers)
            
            with open(outputFilePath, 'w') as out_file:
                for num in sorted_integers:
                    out_file.write(f"{num}\n")
                    
            print(f"Processed {inputFilePath} successfully.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
    
    @staticmethod
    def readNextItemFromFile(line):
        line = line.strip()
        
        # Skip empty lines or lines with more than one integer
        if not line or len(re.findall(r'-?\d+', line)) != 1:
            return None
        
        # Try to convert the line to an integer, skip if conversion fails
        try:
            integer = int(line)
            return integer
        except ValueError:
            return None

def main():
    sample_inputs_dir = '/dsa/hw01/sample_inputs/'
    sample_results_dir = '/dsa/hw01/sample_results/'
    
    # Ensure the result directory exists
    os.makedirs(sample_results_dir, exist_ok=True)
    
    # Process each input file
    for input_filename in os.listdir(sample_inputs_dir):
        input_file_path = os.path.join(sample_inputs_dir, input_filename)
        output_filename = f"{input_filename}_results.txt"
        output_file_path = os.path.join(sample_results_dir, output_filename)
        
        start_time = time.time()
        UniqueInt.processFile(input_file_path, output_file_path)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Processing time for {input_filename}: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()
    
