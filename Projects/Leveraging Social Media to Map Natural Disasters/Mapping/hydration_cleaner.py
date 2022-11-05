#### Code written by Michael Knight
#### functions used by the post_hydration_clean function


import random


# given four sets of coordinates in a bounding box, find a random point within this box
def random_point_within(box):
    
    # find the minimum latitude
    min_x = min(box[0][1], box[1][1], box[2][1], box[3][1])
    
    # find the maximum latitude
    max_x = max(box[0][1], box[1][1], box[2][1], box[3][1])
    
    # find the minimum longitude
    min_y = min(box[0][0], box[1][0], box[2][0], box[3][0])
    
    # find the maximum longitude
    max_y = max(box[0][0], box[1][0], box[2][0], box[3][0]) 

    # find a random point bound by these maximums and minimums
    random_point = [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
    
    
    return random_point



# extracting from one dict - inspired by Josh Robin (augmented by Michael Knight)
def entry_to_extract1(val, thing):
    if (val == None) or (val == 'NaN'):
        return None
    else:
        return val[thing]

# extracting from multiple dicts (specifically only for the 'bounding_box' dict thats in the 'place dict')
# need to extract this list from an extraneous list, and find one random coordinate set from the bounding box.
# The bounding box from the place feature is made up of four points that mark the top/bottom left/right 
# coordinates of the city that the tweet came from.
# inspired by Josh Robin (augmented by Michael Knight)
def entry_to_extract2(val, thing):
    if (val == None) or (val == 'NaN'):
        return None
    else:
        
        # find a random point within the bounding box
        return random_point_within(val['bounding_box'][thing][0])


    
#####################   
# POST HYDRATION CLEANUP
# this drops all of the irrelevant information that we received after hydration

def post_hydration_clean(df):
    
   
    
    # extract coordinates from geo column
    df['geo_coordinates'] = df['geo'].map(lambda x: entry_to_extract1(x, 'coordinates'))
    
    # extract bounding_box coordinates from bounding_box dictionary in the place column
    df['place_coordinates'] = df['place'].map(lambda x: entry_to_extract2(x, 'coordinates'))
    
    
    # when we have coordinates from geo-location in our data, use them
    # if not, use the coordinates approximated by the bounding box from the places column 
    var =[]

    lat1 = []
    long1 = []
    for item in df['geo_coordinates'].iteritems():
        if item[1] != None:
            
            var.append(item[1])
            lat1.append(item[1][0])
            long1.append(item[1][1])
        else:
            
            
             var.append(df['place_coordinates'].iloc[item[0]])
             lat1.append(df['place_coordinates'].iloc[item[0]][0])
             long1.append(df['place_coordinates'].iloc[item[0]][1])

    # set a new column in the dataframe equal to be the value of var
    df['final_coordinates'] = var

    df['lat'] = lat1

    df['long'] = long1
    
    # set the features we want to look at
    features = ['id', 'geo_coordinates', 'created_at', 'full_text', 'place_coordinates', 
                 'place_name', 'final_coordinates', 'lat', 'long'] 


    #replace columns where there are no values for a feature because house doesnt have said feature with 0.0
    df['lat'].fillna(0, inplace=True)

    df['long'].fillna(0, inplace=True)
    
    # set the dataframe to only include the features we are interested in looking at
    df = df[features]
    
    return df # remember to run like this --->      dataframe_name = post_hydration_clean(dataframe_name)
