import csv
import sys
import os

global G    ##global variable initialised
G={}
dic={}      ##dic initialised used in best router function
router=[]   ##router list type initialised usd in best router function



def Creatematrix(fname):   ## function to take text file as input and print it in a matrix format
    global matrix_list
    global matrix_set
    global Graph
    global path
    path=''
    matrix_set = 0
    matrix_list= []
    if fname.endswith('.txt'):



        with open(fname) as fhand:

            matrix_list = [list(map(int,line.split(" "))) for line in fhand]
        matrix_set = 1
    else:
        print "Wrong file extension,Start again,it should be .txt format"  ##validations
        quit()
        if (len(matrix_list)<5):
            print "File should have atleast 5 nodes:"  ##matrix should have more than 10 nodes
            quit()


    print "The topology matrix will be :"   ##printing matrix
    for k in matrix_list:
        for item in k:
            print item,
        print
    print

    Graph = {}            ## Generating graph from matrix
    for i in range(len(matrix_list)):
        temp = {}
        for j in range(len(matrix_list[i])):
            if matrix_list[i][j] != 0 and matrix_list[i][j] != -1:
                temp[j] = matrix_list[i][j]
        Graph[i] = temp

    return Graph

def dijkstra(Graph, Start):    ##function to perform dijkstra algorithm
    global distances
    distances = {}
    global vertices
    vertices={}
    global path
    path = ''

    global previous
    previous = {}

    for v in Graph:
        distances[v] = 9888888777777777777777  ##  Infinity value
        previous[v] = None                      # Previous node in optimal path from source
    distances[Start] = 0                        ##start set to 0 ,so that it is chosen
    for v in Graph:
        vertices[v] = distances[v]
    while vertices:
        for key in vertices:
            if vertices[key] < distances[key]:
                distances[key] = vertices[key]
                previous[key] = key
        del vertices[key]
        u = key
        for v in Graph[u].keys():             # for each neighbor of u

            w = Graph[u][v]                     # distance from u to v

            latest_dist = distances[u] + w
            if (latest_dist < distances[v]):     # is new distance shorter than one in dist, Then we need to save latest dist
                vertices[v] = latest_dist
                distances[v] = latest_dist
                previous[v] = u
    return distances,previous

def printpath(Start,previous,destination):   ##function to print previous path
    print "Shortest path from Source router to Destination router:"
    path=''
    x = destination


    while x != Start:
        path = path + str(x) + ">-"   ##from destination to start we are printing the path using previous


        x = previous[x]
    path = path + str(Start)
    print path[::-1]


###.................Actual Program............Starts.................................
print "........................................................................"
#print "Welcome to Link State Routing Simulator"
print "1->Input the text file and print it in matrix format"
#print "2->To print the connection table of your source router"
print "3->To print the total cost,shortest path between your source and destination router "
#print "4->To delete a router"
#print "5->To print the best router"
#print "6->Program Exit"
print "Press Y to return to Main Menu"
print "............................................................................"
c=1
while True:   ##infinity loop
  try:
   n = (int(raw_input("Master Command:")))
  except :
      print "Enter Number Only...Exiting......try again..."
      quit()

  if n!=1 and c==1:                   ##to validate that no other options can be executed before option 1
    print "Please insert the matrix first"
    continue
  else:
    c=0

  if n==1:
    fname=raw_input("Input Original Network Topology Matrix File :") ####main funtion for option 1 ,matrix printed

    G=Creatematrix(fname)
  ## connectiontable called to print the coonection table

  elif n==3:
                             ## to show cost and the best path


    try:

     Start1 = int(raw_input("Enter Start Router:"))


     destination = int(raw_input("Enter Destination Router:"))
    except:
        print "integers only"
        quit()
    dist_A, previous = dijkstra(G, Start1)
    print "Total Cost from Source router to Destination router:" ##code to find the cost
    for v in dist_A:
        if v == destination:
            print Start1, '->', destination
            print 'Cost:',dist_A[v]
    printpath(Start1, previous, destination) ##printpath
 
  elif n>6:                     ##to check options dont exceed 6
      print "Options Exceeded....."
      break
  return_to_menu = raw_input("Return to Main Menu,y/n:")
  if return_to_menu != 'y':

      print "Sorry ,Wrong Choice.....The program terminates......"
      break
