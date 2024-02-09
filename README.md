# Command Line Web Radio Player  
  
A simple command line tool for managing and listening to web radio stations on Linux.  
  
## Dependencies  
  
This script depends on `mpg123`, a command-line audio player. You can install it using the package manager for your distribution, for example:  
  
```bash  
sudo apt-get install mpg123  # On Ubuntu or Debian  
sudo yum install mpg123      # On Fedora or CentOS  
```  
  
The script is easy to modify if you want to use a different command-line audio player.  
  
## Usage  
  
1. Create a text file (e.g. `stations.txt`) with your favorite radio stations in the following format:  
  
```  
[key] "Station Name" http://streaming-url.com  
```  
  
For example:  
  
```  
[inter] "France Inter" http://direct.franceinter.fr/live/franceinter-midfi.mp3  
[canada] "Radio Canada" https://playerservices.streamtheworld.com/api/livestream-redirect/CBFFM_SRC.mp3  
[fip] "FIP" http://direct.fipradio.fr/live/fip-midfi.mp3  
```  
  
2. Run the script with one of the following command line arguments:  
  
- `on`: Start playing the default radio station.  
- `off`: Stop playing the radio.  
- `station_key`: Start playing the radio station with the specified key from the `stations.txt` file.  
  
For example:  
  
```bash  
python script.py on        # Start playing the default radio station  
python script.py off       # Stop playing the radio  
python script.py inter     # Start playing the "France Inter" radio station  
```  
  
## Customization  
  
You can add, modify, or remove radio stations in the `stations.txt` file to customize the list of available stations. The script will automatically load the updated stations without any further modifications.  
  
## Creating an Alias  
  
To make it more convenient to use, you can add an alias to your `.profile` or `.bashrc` file. Open the file with your favorite text editor (e.g., `nano` or `vim`) and add the following line:  
  
```bash  
alias radio='python /path/to/script.py'  
```  

Replace /path/to/script.py with the actual path to the script on your system. Save and close the file, then run source .profile or source .bashrc to apply the changes. Now, you can use the radio command instead of typing the full python script.py command.

### Usage Examples with Alias
 
Here are some examples of how to use the radio alias:
```bash  
radio on        # Start playing the default radio station  
```  
```bash  
radio off       # Stop playing the radio  
```  
```bash  
radio inter     # Start playing the "France Inter" radio station  
```  
