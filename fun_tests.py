list = ['xxx/A.B','y/C.D','z/E.F','44/G.H']
nb_files = len(list)
fetched_list = []
inner_list = []

test_list = [[] for i in range(nb_files)]
#print (test_list)

def split_list (list, new_list):
    for item in list:
        name_start_index = (item.rfind('/'))+1
        format_index = (item.rfind('.'))
        format_start_index = format_index +1
        name = item[name_start_index:format_index]
        format = item[format_start_index:]

        pair = [name,format]
        fetched_list.append(pair )
    print (fetched_list)

split_list(list,fetched_list)


#alphabet = "abcdefghijklmnopqrstuvwxyz"
#nested_list = []
#for i in range(0, len(alphabet), 2):
#    pair = [alphabet[i], alphabet[i+1]]
#    nested_list.append(pair)
#print(nested_list)

#lambda function test
varA= 'A',
varB = 'B',
var5 = 5,
var8 = 8,
func = lambda x,y: x + y
print ("lambda function test:")
print (func (var5,var8))