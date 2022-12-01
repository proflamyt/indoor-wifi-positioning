# Indoor localization using Wireless access points
    

#### Video Demo:  <https://youtu.be/e-RHlSTMgfE>
#### Description:

Takes in an access point name as a command line argument and measures the distance between the said access point and the device using RSSI (Received Signal Strength Indicator) .

RSSI stands for Received Signal Strength Indicator. It is an estimated measure of power level that an RF client device is receiving from an access point or router. At larger distances, the signal gets weaker and the wireless data rates get slower, leading to a lower overall data throughput.
The RSSI is measured in dBm and is a negative value. The closer to 0 the better the signal is.

Locating objects or people around the world has been prominent for a while now thanks to GPS, although the localization of this is suitable in areas where acurrate point can be overlooked, that is not the case for indoor localization, cause of it small scale GPS can not locate internally . This is where indoor localization comes in, to be able to know where an object or a person is in a small area, diffrent access points can be positioned around the house and the object in question made to connect with it, the distance between the access point and the object is measured using the signal strenght.

First the object scans for the access points around its areas and picks their signal strenght, then it picks out the known access points from the scanned ones , that is , the ones you specifially positioned , and measures the distance between each 0f these access points 



## Usage 

```
python project.py -l "access point"

```


## Test

```
pytest

```