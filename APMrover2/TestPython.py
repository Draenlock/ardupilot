import subprocess

process = subprocess.Popen(['sim_vehicle.py', '--map', '-L' ,'Polytech'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

'''
NE PAS ENLEVER C'est la commande qui est utilisé dans OA_CSA.cpp, c'est une backup si au cas ou je perd l'autre
    gcs().send_text(MAV_SEVERITY_INFO, "current_loc : LAT %d LONG %d",current_loc.lat,current_loc.lng);
'''
'''
Commandes SITL
param set SIM_WIND_DIR x <- Direction du vent en °
param set SIM_WIND_SPD x <- en m.s-1 ( je crois )

communicate
'''
while True:
    output = process.stdout.readline()
    arraySplit = output.split()
    lat = 0
    lon = 0
    #process.call(["arm", "throttle"])
    print(output.strip())
    #print(type(output.strip()))
    if output.strip().find("current_loc") != -1:
        for index in range(len(arraySplit)):
            if arraySplit[index] == 'LAT':
                lat = arraySplit[index+1]
            if arraySplit[index] == 'LONG':
                lon = arraySplit[index+1]
                process.communicate("param set SIM_WIND_DIR 0")
        print(lat)  ## Valeur Lattitude
        print(lon)  ## Valeur Longitude
        
    #   print('YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO3')
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break

