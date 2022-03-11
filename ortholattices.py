#from poalgs import Model
from provers import Model, prover9

O=[
Model(cardinality = 6, index = 0, operations = {
"+":[
[0,1,2,3,4,5],
[1,1,1,1,1,1],
[2,1,2,1,1,1],
[3,1,1,3,1,1],
[4,1,1,1,4,1],
[5,1,1,1,1,5]], 
"*":[
[0,0,0,0,0,0],
[0,1,2,3,4,5],
[0,2,2,0,0,0],
[0,3,0,3,0,0],
[0,4,0,0,4,0],
[0,5,0,0,0,5]], "'":[1, 0, 3, 2, 5, 4]}), 
Model(cardinality = 8, index = 1, operations = {
"+":[
[0,1,2,3,4,5,6,7],
[1,1,1,1,1,1,1,1],
[2,1,2,1,1,1,1,2],
[3,1,1,3,6,1,6,1],
[4,1,1,6,4,1,6,1],
[5,1,1,1,1,5,1,5],
[6,1,1,6,6,1,6,1],
[7,1,2,1,1,5,1,7]], 
"*":[
[0,0,0,0,0,0,0,0],
[0,1,2,3,4,5,6,7],
[0,2,2,0,0,7,0,7],
[0,3,0,3,0,0,3,0],
[0,4,0,0,4,0,4,0],
[0,5,7,0,0,5,0,7],
[0,6,0,3,4,0,6,0],
[0,7,7,0,0,7,0,7]], "'":[1, 0, 3, 2, 5, 4, 7, 6]}), 
Model(cardinality = 10, index = 2, operations = {
"+":[
[0,1,2,3,4,5,6,7,8,9],
[1,1,1,1,1,1,1,1,1,1],
[2,1,2,1,1,1,1,2,1,1],
[3,1,1,3,6,1,6,1,6,1],
[4,1,1,6,4,1,6,9,6,9],
[5,1,1,1,1,5,1,5,5,1],
[6,1,1,6,6,1,6,1,6,1],
[7,1,2,1,9,5,1,7,5,9],
[8,1,1,6,6,5,6,5,8,1],
[9,1,1,1,9,1,1,9,1,9]], 
"*":[
[0,0,0,0,0,0,0,0,0,0],
[0,1,2,3,4,5,6,7,8,9],
[0,2,2,0,0,7,0,7,0,7],
[0,3,0,3,0,0,3,0,0,0],
[0,4,0,0,4,0,4,0,0,4],
[0,5,7,0,0,5,8,7,8,7],
[0,6,0,3,4,8,6,0,8,4],
[0,7,7,0,0,7,0,7,0,7],
[0,8,0,0,0,8,8,0,8,0],
[0,9,7,0,4,7,4,7,0,9]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9, 8]}), 
Model(cardinality = 10, index = 3, operations = {
"+":[
[0,1,2,3,4,5,6,7,8,9],
[1,1,1,1,1,1,1,1,1,1],
[2,1,2,1,1,2,2,1,1,2],
[3,1,1,3,4,1,8,7,8,7],
[4,1,1,4,4,1,8,1,8,1],
[5,1,2,1,1,5,2,1,1,5],
[6,1,2,8,8,2,6,1,8,2],
[7,1,1,7,1,1,1,7,1,7],
[8,1,1,8,8,1,8,1,8,1],
[9,1,2,7,1,5,2,7,1,9]], 
"*":[
[0,0,0,0,0,0,0,0,0,0],
[0,1,2,3,4,5,6,7,8,9],
[0,2,2,0,0,5,6,9,6,9],
[0,3,0,3,3,0,0,3,3,0],
[0,4,0,3,4,0,0,3,4,0],
[0,5,5,0,0,5,0,9,0,9],
[0,6,6,0,0,0,6,0,6,0],
[0,7,9,3,3,9,0,7,3,9],
[0,8,6,3,4,0,6,3,8,0],
[0,9,9,0,0,9,0,9,0,9]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9, 8]}), 
Model(cardinality = 10, index = 4, operations = {
"+":[
[0,1,2,3,4,5,6,7,8,9],
[1,1,1,1,1,1,1,1,1,1],
[2,1,2,1,1,2,2,1,1,2],
[3,1,1,3,4,1,8,7,8,7],
[4,1,1,4,4,1,8,7,8,7],
[5,1,2,1,1,5,5,1,1,5],
[6,1,2,8,8,5,6,1,8,5],
[7,1,1,7,7,1,1,7,1,7],
[8,1,1,8,8,1,8,1,8,1],
[9,1,2,7,7,5,5,7,1,9]], 
"*":[
[0,0,0,0,0,0,0,0,0,0],
[0,1,2,3,4,5,6,7,8,9],
[0,2,2,0,0,5,6,9,6,9],
[0,3,0,3,3,0,0,3,3,0],
[0,4,0,3,4,0,0,4,4,0],
[0,5,5,0,0,5,6,9,6,9],
[0,6,6,0,0,6,6,0,6,0],
[0,7,9,3,4,9,0,7,4,9],
[0,8,6,3,4,6,6,4,8,0],
[0,9,9,0,0,9,0,9,0,9]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9, 8]}), 
Model(cardinality = 12, index = 5, operations = {
"+":[
[ 0,1,2,3,4, 5,6, 7,8,9,10,11],
[ 1,1,1,1,1, 1,1, 1,1,1, 1, 1],
[ 2,1,2,1,1, 2,6, 1,1,6, 1, 6],
[ 3,1,1,3,4, 1,1, 3,4,1, 4, 1],
[ 4,1,1,4,4, 1,1, 4,4,1, 4, 1],
[ 5,1,2,1,1, 5,6, 1,1,9, 1,11],
[ 6,1,6,1,1, 6,6, 1,1,6, 1, 6],
[ 7,1,1,3,4, 1,1, 7,8,1,10, 1],
[ 8,1,1,4,4, 1,1, 8,8,1, 4, 1],
[ 9,1,6,1,1, 9,6, 1,1,9, 1, 6],
[10,1,1,4,4, 1,1,10,4,1,10, 1],
[11,1,6,1,1,11,6, 1,1,6, 1,11]], 
"*":[
[0, 0,0,0, 0,0, 0,0,0,0, 0, 0],
[0, 1,2,3, 4,5, 6,7,8,9,10,11],
[0, 2,2,0, 0,5, 2,0,0,5, 0, 5],
[0, 3,0,3, 3,0, 0,7,7,0, 7, 0],
[0, 4,0,3, 4,0, 0,7,8,0,10, 0],
[0, 5,5,0, 0,5, 5,0,0,5, 0, 5],
[0, 6,2,0, 0,5, 6,0,0,9, 0,11],
[0, 7,0,7, 7,0, 0,7,7,0, 7, 0],
[0, 8,0,7, 8,0, 0,7,8,0, 7, 0],
[0, 9,5,0, 0,5, 9,0,0,9, 0, 5],
[0,10,0,7,10,0, 0,7,7,0,10, 0],
[0,11,5,0, 0,5,11,0,0,5, 0,11]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]}), 
Model(cardinality = 12, index = 6, operations = {
"+":[
[ 0,1,2,3,4,5,6, 7,8, 9,10,11],
[ 1,1,1,1,1,1,1, 1,1, 1, 1, 1],
[ 2,1,2,1,1,2,6, 1,1, 2, 6, 1],
[ 3,1,1,3,4,1,1, 3,8, 1, 1, 8],
[ 4,1,1,4,4,1,1, 4,8, 1, 1, 8],
[ 5,1,2,1,1,5,6, 1,1, 5, 6, 1],
[ 6,1,6,1,1,6,6, 1,1, 6, 6, 1],
[ 7,1,1,3,4,1,1, 7,8, 1, 1,11],
[ 8,1,1,8,8,1,1, 8,8, 1, 1, 8],
[ 9,1,2,1,1,5,6, 1,1, 9,10, 1],
[10,1,6,1,1,6,6, 1,1,10,10, 1],
[11,1,1,8,8,1,1,11,8, 1, 1,11]], 
"*":[
[0, 0,0,0,0,0, 0,0, 0,0, 0, 0],
[0, 1,2,3,4,5, 6,7, 8,9,10,11],
[0, 2,2,0,0,5, 2,0, 0,9, 9, 0],
[0, 3,0,3,3,0, 0,7, 3,0, 0, 7],
[0, 4,0,3,4,0, 0,7, 4,0, 0, 7],
[0, 5,5,0,0,5, 5,0, 0,9, 9, 0],
[0, 6,2,0,0,5, 6,0, 0,9,10, 0],
[0, 7,0,7,7,0, 0,7, 7,0, 0, 7],
[0, 8,0,3,4,0, 0,7, 8,0, 0,11],
[0, 9,9,0,0,9, 9,0, 0,9, 9, 0],
[0,10,9,0,0,9,10,0, 0,9,10, 0],
[0,11,0,7,7,0, 0,7,11,0, 0,11]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10]}),
Model(cardinality = 14, index = 310, operations = {
"+":[
[ 0,1,2,3, 4,5,6, 7,8, 9,10,11,12,13],
[ 1,1,1,1, 1,1,1, 1,1, 1, 1, 1, 1, 1],
[ 2,1,2,1, 1,5,1, 2,1, 2, 1, 5, 1, 5],
[ 3,1,1,3, 3,1,6, 8,8, 6, 8, 6, 6, 8],
[ 4,1,1,3, 4,1,6,10,8,12,10, 6,12, 8],
[ 5,1,5,1, 1,5,1, 5,1, 5, 1, 5, 1, 5],
[ 6,1,1,6, 6,1,6, 1,1, 6, 1, 6, 6, 1],
[ 7,1,2,8,10,5,1, 7,8, 2,10, 5, 1,13],
[ 8,1,1,8, 8,1,1, 8,8, 1, 8, 1, 1, 8],
[ 9,1,2,6,12,5,6, 2,1, 9, 1,11,12, 5],
[10,1,1,8,10,1,1,10,8, 1,10, 1, 1, 8],
[11,1,5,6, 6,5,6, 5,1,11, 1,11, 6, 5],
[12,1,1,6,12,1,6, 1,1,12, 1, 6,12, 1],
[13,1,5,8, 8,5,1,13,8, 5, 8, 5, 1,13]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9,
8, 11, 10, 13, 12]}),
Model(cardinality = 14, index = 289, operations = {
"+":[
[ 0,1,2,3,4, 5,6, 7,8, 9,10,11,12,13],
[ 1,1,1,1,1, 1,1, 1,1, 1, 1, 1, 1, 1],
[ 2,1,2,1,1, 6,6, 1,1, 2, 1, 6, 6, 1],
[ 3,1,1,3,1, 8,1, 3,8, 1, 8, 1, 1, 8],
[ 4,1,1,1,4, 1,1, 4,1, 4, 1, 4, 1, 4],
[ 5,1,6,8,1, 5,6,10,8,12,10, 6,12, 8],
[ 6,1,6,1,1, 6,6, 1,1, 6, 1, 6, 6, 1],
[ 7,1,1,3,4,10,1, 7,8, 4,10, 4, 1,13],
[ 8,1,1,8,1, 8,1, 8,8, 1, 8, 1, 1, 8],
[ 9,1,2,1,4,12,6, 4,1, 9, 1,11,12, 4],
[10,1,1,8,1,10,1,10,8, 1,10, 1, 1, 8],
[11,1,6,1,4, 6,6, 4,1,11, 1,11, 6, 4],
[12,1,6,1,1,12,6, 1,1,12, 1, 6,12, 1],
[13,1,1,8,4, 8,1,13,8, 4, 8, 4, 1,13]], "'":[1, 0, 3, 2, 5, 4, 7, 6, 9,
8, 11, 10, 13, 12]}), 
Model(cardinality = 18, index = 12, operations = {
"+":[
[ 0, 1,2, 3,4, 5,6,7,8,9,10,11,12,13,14,15,16,17],
[ 1, 1,2, 6,4, 5,6,7,8,9, 9, 9,12, 9, 8,12, 6, 5],
[ 2, 2,2, 6,4, 7,6,7,8,9, 9, 9, 7, 9, 8, 7, 6, 7],
[ 3, 6,6, 3,8, 9,6,9,8,9,10,10, 9,10,14,10, 3,10],
[ 4, 4,4, 8,4, 7,8,7,8,9, 9, 9, 7, 9, 8, 7, 8, 7],
[ 5, 5,7, 9,7, 5,9,7,9,9, 9, 9,12, 9, 9,12, 9, 5],
[ 6, 6,6, 6,8, 9,6,9,8,9, 9, 9, 9, 9, 8, 9, 6, 9],
[ 7, 7,7, 9,7, 7,9,7,9,9, 9, 9, 7, 9, 9, 7, 9, 7],
[ 8, 8,8, 8,8, 9,8,9,8,9, 9, 9, 9, 9, 8, 9, 8, 9],
[ 9, 9,9, 9,9, 9,9,9,9,9, 9, 9, 9, 9, 9, 9, 9, 9],
[10, 9,9,10,9, 9,9,9,9,9,10,10, 9,10,10,10,10,10],
[11, 9,9,10,9, 9,9,9,9,9,10,11, 9,11,10,11,11,11],
[12,12,7, 9,7,12,9,7,9,9, 9, 9,12, 9, 9,12, 9,12],
[13, 9,9,10,9, 9,9,9,9,9,10,11, 9,13,10,11,13,13],
[14, 8,8,14,8, 9,8,9,8,9,10,10, 9,10,14,10,14,10],
[15,12,7,10,7,12,9,7,9,9,10,11,12,11,10,15,11,15],
[16, 6,6, 3,8, 9,6,9,8,9,10,11, 9,13,14,11,16,13],
[17, 5,7,10,7, 5,9,7,9,9,10,11,12,13,10,15,13,17]], "'":[9, 10, 11, 12,
13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8]})]

H = Model(cardinality = 6, index = 0, operations = {"'":[1, 0, 3, 2, 5, 4], 
"+":[
[0,1,2,3,4,5],
[1,1,1,1,1,1],
[2,1,2,1,1,5],
[3,1,1,3,3,1],
[4,1,1,3,4,1],
[5,1,5,1,1,5]],
"*":[
[0,0,0,0,0,0],
[0,1,2,3,4,5],
[0,2,2,0,0,2],
[0,3,0,3,4,0],
[0,4,0,4,4,0],
[0,5,2,0,0,5]]})

M4=O[0]

def meetOL(A):
    jn = A.operations["+"]
    c = A.operations["'"]
    B = range(A.cardinality)
    return [[c[jn[c[i]][c[j]]] for i in B] for j in B]

for A in O:
  if "*" not in A.operations.keys(): A.operations["*"]=meetOL(A)

L=[
Model(cardinality = 5, index = 16, operations = { #N
"*":[
[0,0,0,0,0],
[0,1,0,1,1],
[0,0,2,0,2],
[0,1,0,3,3],
[0,1,2,3,4]], 
"+":[
[0,1,2,3,4],
[1,1,4,3,4],
[2,4,2,4,4],
[3,3,4,3,4],
[4,4,4,4,4]]}), 
Model(cardinality = 5, index = 0, operations = { #M3
"*":[
[0,0,0,0,0],
[0,1,0,0,1],
[0,0,2,0,2],
[0,0,0,3,3],
[0,1,2,3,4]], 
"+":[
[0,1,2,3,4],
[1,1,4,4,4],
[2,4,2,4,4],
[3,4,4,3,4],
[4,4,4,4,4]]}), 
Model(cardinality = 6, index = 5, operations = { #L5
"*":[
[0,0,0,0,0,0],
[0,1,0,1,1,1],
[0,0,2,0,0,2],
[0,1,0,3,1,3],
[0,1,0,1,4,4],
[0,1,2,3,4,5]], 
"+":[
[0,1,2,3,4,5],
[1,1,5,3,4,5],
[2,5,2,5,5,5],
[3,3,5,3,5,5],
[4,4,5,5,4,5],
[5,5,5,5,5,5]]}), 
Model(cardinality = 6, index = 4, operations = { #L4
"*":[
[0,0,0,0,0,0],
[0,1,0,0,1,1],
[0,0,2,0,2,2],
[0,0,0,3,0,3],
[0,1,2,0,4,4],
[0,1,2,3,4,5]], 
"+":[
[0,1,2,3,4,5],
[1,1,4,5,4,5],
[2,4,2,5,4,5],
[3,5,5,3,5,5],
[4,4,4,5,4,5],
[5,5,5,5,5,5]]}), 
Model(cardinality = 7, index = 2, operations = { #L2
"*":[
[0,0,0,0,0,0,0],
[0,1,0,1,0,1,1],
[0,0,2,0,2,2,2],
[0,1,0,3,0,1,3],
[0,0,2,0,4,2,4],
[0,1,2,1,2,5,5],
[0,1,2,3,4,5,6]], 
"+":[
[0,1,2,3,4,5,6],
[1,1,5,3,6,5,6],
[2,5,2,6,4,5,6],
[3,3,6,3,6,6,6],
[4,6,4,6,4,6,6],
[5,5,5,6,6,5,6],
[6,6,6,6,6,6,6]]}), 
Model(cardinality = 7, index = 3, operations = { #L3
"*":[
[0,0,0,0,0,0,0],
[0,1,0,1,1,1,1],
[0,0,2,0,0,2,2],
[0,1,0,3,1,3,3],
[0,1,0,1,4,1,4],
[0,1,2,3,1,5,5],
[0,1,2,3,4,5,6]], 
"+":[
[0,1,2,3,4,5,6],
[1,1,5,3,4,5,6],
[2,5,2,5,6,5,6],
[3,3,5,3,6,5,6],
[4,4,6,6,4,6,6],
[5,5,5,5,6,5,6],
[6,6,6,6,6,6,6]]}), 
Model(cardinality = 7, index = 1, operations = {
"*":[
[0,0,0,0,0,0,0],
[0,1,0,0,1,1,1],
[0,0,2,0,2,0,2],
[0,0,0,3,0,3,3],
[0,1,2,0,4,1,4],
[0,1,0,3,1,5,5],
[0,1,2,3,4,5,6]], 
"+":[
[0,1,2,3,4,5,6],
[1,1,4,5,4,5,6],
[2,4,2,6,4,6,6],
[3,5,6,3,6,5,6],
[4,4,4,6,4,6,6],
[5,5,6,5,6,5,6],
[6,6,6,6,6,6,6]]}), 
Model(cardinality = 8, index = 6, operations = {
"*":[
[0,0,0,0,0,0,0,0],
[0,1,1,1,1,0,1,1],
[0,1,2,1,2,0,2,2],
[0,1,1,3,1,0,3,3],
[0,1,2,1,4,0,4,4],
[0,0,0,0,0,5,0,5],
[0,1,2,3,4,0,6,6],
[0,1,2,3,4,5,6,7]], 
"+":[
[0,1,2,3,4,5,6,7],
[1,1,2,3,4,7,6,7],
[2,2,2,6,4,7,6,7],
[3,3,6,3,6,7,6,7],
[4,4,4,6,4,7,6,7],
[5,7,7,7,7,5,7,7],
[6,6,6,6,6,7,6,7],
[7,7,7,7,7,7,7,7]]}), 
Model(cardinality = 9, index = 14, operations = {
"*":[
[0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,1,1],
[0,0,2,0,2,0,2,2,2],
[0,0,0,3,0,3,3,0,3],
[0,1,2,0,4,1,2,4,4],
[0,1,0,3,1,5,3,1,5],
[0,0,2,3,2,3,6,2,6],
[0,1,2,0,4,1,2,7,7],
[0,1,2,3,4,5,6,7,8]], 
"+":[
[0,1,2,3,4,5,6,7,8],
[1,1,4,5,4,5,8,7,8],
[2,4,2,6,4,8,6,7,8],
[3,5,6,3,8,5,6,8,8],
[4,4,4,8,4,8,8,7,8],
[5,5,8,5,8,5,8,8,8],
[6,8,6,6,8,8,6,8,8],
[7,7,7,8,7,8,8,7,8],
[8,8,8,8,8,8,8,8,8]]}), 
Model(cardinality = 9, index = 13, operations = {
"*":[
[0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,0,1,1,1],
[0,0,2,0,0,2,2,0,2],
[0,0,0,3,0,3,0,3,3],
[0,1,0,0,4,0,4,4,4],
[0,0,2,3,0,5,2,3,5],
[0,1,2,0,4,2,6,4,6],
[0,1,0,3,4,3,4,7,7],
[0,1,2,3,4,5,6,7,8]], 
"+":[
[0,1,2,3,4,5,6,7,8],
[1,1,6,7,4,8,6,7,8],
[2,6,2,5,6,5,6,8,8],
[3,7,5,3,7,5,8,7,8],
[4,4,6,7,4,8,6,7,8],
[5,8,5,5,8,5,8,8,8],
[6,6,6,8,6,8,6,8,8],
[7,7,8,7,7,8,8,7,8],
[8,8,8,8,8,8,8,8,8]]}), 
Model(cardinality = 9, index = 10, operations = {
"*":[
[0,0,0,0,0,0,0,0,0],
[0,1,0,1,1,1,0,1,1],
[0,0,2,0,2,0,2,2,2],
[0,1,0,3,1,3,0,3,3],
[0,1,2,1,4,1,2,4,4],
[0,1,0,3,1,5,0,5,5],
[0,0,2,0,2,0,6,2,6],
[0,1,2,3,4,5,2,7,7],
[0,1,2,3,4,5,6,7,8]], 
"+":[
[0,1,2,3,4,5,6,7,8],
[1,1,4,3,4,5,8,7,8],
[2,4,2,7,4,7,6,7,8],
[3,3,7,3,7,5,8,7,8],
[4,4,4,7,4,7,8,7,8],
[5,5,7,5,7,5,8,7,8],
[6,8,6,8,8,8,6,8,8],
[7,7,7,7,7,7,8,7,8],
[8,8,8,8,8,8,8,8,8]]}), 
Model(cardinality = 9, index = 8, operations = {
"*":[
[0,0,0,0,0,0,0,0,0],
[0,1,0,1,1,1,0,1,1],
[0,0,2,2,0,2,2,2,2],
[0,1,2,3,1,3,2,3,3],
[0,1,0,1,4,1,0,4,4],
[0,1,2,3,1,5,2,5,5],
[0,0,2,2,0,2,6,2,6],
[0,1,2,3,4,5,2,7,7],
[0,1,2,3,4,5,6,7,8]], 
"+":[
[0,1,2,3,4,5,6,7,8],
[1,1,3,3,4,5,8,7,8],
[2,3,2,3,7,5,6,7,8],
[3,3,3,3,7,5,8,7,8],
[4,4,7,7,4,7,8,7,8],
[5,5,5,5,7,5,8,7,8],
[6,8,6,8,8,8,6,8,8],
[7,7,7,7,7,7,8,7,8],
[8,8,8,8,8,8,8,8,8]]}), 
Model(cardinality = 9, index = 9, operations = {
"*":[
[0,0,0,0,0,0,0,0,0],
[0,1,1,1,0,1,1,1,1],
[0,1,2,1,0,2,1,2,2],
[0,1,1,3,0,1,3,3,3],
[0,0,0,0,4,0,4,0,4],
[0,1,2,1,0,5,1,5,5],
[0,1,1,3,4,1,6,3,6],
[0,1,2,3,0,5,3,7,7],
[0,1,2,3,4,5,6,7,8]], 
"+":[
[0,1,2,3,4,5,6,7,8],
[1,1,2,3,6,5,6,7,8],
[2,2,2,7,8,5,8,7,8],
[3,3,7,3,6,7,6,7,8],
[4,6,8,6,4,8,6,8,8],
[5,5,5,7,8,5,8,7,8],
[6,6,8,6,6,8,6,8,8],
[7,7,7,7,8,7,8,7,8],
[8,8,8,8,8,8,8,8,8]]}), 
Model(cardinality = 9, index = 7, operations = {
"*":[
[0,0,0,0,0,0,0,0,0],
[0,1,1,1,0,1,1,1,1],
[0,1,2,2,0,1,2,2,2],
[0,1,2,3,0,1,3,3,3],
[0,0,0,0,4,0,4,0,4],
[0,1,1,1,0,5,1,5,5],
[0,1,2,3,4,1,6,3,6],
[0,1,2,3,0,5,3,7,7],
[0,1,2,3,4,5,6,7,8]], 
"+":[
[0,1,2,3,4,5,6,7,8],
[1,1,2,3,6,5,6,7,8],
[2,2,2,3,6,7,6,7,8],
[3,3,3,3,6,7,6,7,8],
[4,6,6,6,4,8,6,8,8],
[5,5,7,7,8,5,8,7,8],
[6,6,6,6,6,8,6,8,8],
[7,7,7,7,8,7,8,7,8],
[8,8,8,8,8,8,8,8,8]]}), 
Model(cardinality = 10, index = 12, operations = {
"*":[
[0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,1,0,1,1,1,1],
[0,0,2,0,2,2,2,0,2,2],
[0,1,0,3,1,0,3,3,3,3],
[0,1,2,1,4,2,4,1,4,4],
[0,0,2,0,2,5,2,0,5,5],
[0,1,2,3,4,2,6,3,6,6],
[0,1,0,3,1,0,3,7,3,7],
[0,1,2,3,4,5,6,3,8,8],
[0,1,2,3,4,5,6,7,8,9]], 
"+":[
[0,1,2,3,4,5,6,7,8,9],
[1,1,4,3,4,8,6,7,8,9],
[2,4,2,6,4,5,6,9,8,9],
[3,3,6,3,6,8,6,7,8,9],
[4,4,4,6,4,8,6,9,8,9],
[5,8,5,8,8,5,8,9,8,9],
[6,6,6,6,6,8,6,9,8,9],
[7,7,9,7,9,9,9,7,9,9],
[8,8,8,8,8,8,8,9,8,9],
[9,9,9,9,9,9,9,9,9,9]]}), 
Model(cardinality = 10, index = 11, operations = {
"*":[
[0,0,0,0,0,0,0,0,0,0],
[0,1,1,0,1,1,1,1,1,1],
[0,1,2,0,2,1,2,2,2,2],
[0,0,0,3,0,0,3,0,3,3],
[0,1,2,0,4,1,2,4,4,4],
[0,1,1,0,1,5,1,5,1,5],
[0,1,2,3,2,1,6,2,6,6],
[0,1,2,0,4,5,2,7,4,7],
[0,1,2,3,4,1,6,4,8,8],
[0,1,2,3,4,5,6,7,8,9]], 
"+":[
[0,1,2,3,4,5,6,7,8,9],
[1,1,2,6,4,5,6,7,8,9],
[2,2,2,6,4,7,6,7,8,9],
[3,6,6,3,8,9,6,9,8,9],
[4,4,4,8,4,7,8,7,8,9],
[5,5,7,9,7,5,9,7,9,9],
[6,6,6,6,8,9,6,9,8,9],
[7,7,7,9,7,7,9,7,9,9],
[8,8,8,8,8,9,8,9,8,9],
[9,9,9,9,9,9,9,9,9,9]]}), 
Model(cardinality = 10, index = 15, operations = {
"*":[
[0,0,0,0,0,0,0,0,0,0],
[0,1,0,1,1,1,0,1,1,1],
[0,0,2,2,2,0,2,2,2,2],
[0,1,2,3,3,1,2,3,3,3],
[0,1,2,3,4,1,2,4,4,4],
[0,1,0,1,1,5,0,5,1,5],
[0,0,2,2,2,0,6,2,6,6],
[0,1,2,3,4,5,2,7,4,7],
[0,1,2,3,4,1,6,4,8,8],
[0,1,2,3,4,5,6,7,8,9]], 
"+":[
[0,1,2,3,4,5,6,7,8,9],
[1,1,3,3,4,5,8,7,8,9],
[2,3,2,3,4,7,6,7,8,9],
[3,3,3,3,4,7,8,7,8,9],
[4,4,4,4,4,7,8,7,8,9],
[5,5,7,7,7,5,9,7,9,9],
[6,8,6,8,8,9,6,9,8,9],
[7,7,7,7,7,7,9,7,9,9],
[8,8,8,8,8,9,8,9,8,9],
[9,9,9,9,9,9,9,9,9,9]]})]

L=sorted(L,key=lambda x: x.index)

M3=L[0]
N=L[16]

def product(self, B, info=False):
        base = [[x,y] for x in range(self.cardinality) for y in range (B.cardinality)]
        if info: print(base)
        op = {}
        for f in B.operations:
            fA = self.operations[f]
            fB = B.operations[f]
            if type(fB)==list:
                if type(fB[0])==list:
                    op[f] = [[base.index([fA[p[0]][q[0]],fB[p[1]][q[1]]])
                               for p in base] for q in base]
                else:
                    op[f] = [base.index([fA[p[0]],fB[p[1]]]) for p in base]
            else:
                op[f] = base.index([fA,fB])
        rel = {}
        for r in B.relations:
            rA = self.relations[r]
            rB = B.relations[r]
            if type(rB[0])==list:
                rel[r] = [[1 if rA[p[0]][q[0]]==1 and rB[p[1]][q[1]]==1 else 0
                             for p in base] for q in base]
            else:
                rel[r] =[1 if rA[p[0]]==1 and rB[p[1]]==1 else 0 for p in base]
        return Model(len(base),None,op,rel)

Model.product = product

def check(structure,FOformula_list,info=False):
  if type(FOformula_list)==str: FOformula_list=[FOformula_list]
  for st in FOformula_list:
    lt = []
    if "<=" in st:
      if "+" in st: lt = ["x<=y <-> x+y=y"]
      if "*" in st: lt = ["x<=y <-> x*y=x"]
      if "v" in st: lt = ["x<=y <-> x v y=y"]
      if "^" in st: lt = ["x<=y <-> x^y=x"]
    li = prover9(structure.diagram("")+lt,[st],1000,0,structure.cardinality,one=True)
    if li!=[]:
      if info: return li+[st+" fails"]
      return False
  return True #li==[]

def show(li,symbols="<= +", unaryRel=""):
    if type(li)!=list: li = [li]
    # use graphviz to display a mace4 structure as a diagram
    # symbols is a list of binary symbols that define a poset or graph
    # unaryRel is a unary relation symbol that is displayed by red nodes
    i = 0
    sy = symbols.split(" ")
    #print(sy)
    st = ""
    for x in li:
        i+=1
        st+=str(i)
        uR = x.relations[unaryRel] if unaryRel!="" else [0]*x.cardinality
        for s in sy:
            t = s[:-1] if s[-1]=='d' else s
            if t in x.operations.keys():
                st+=hasse_diagram(x.operations[t],False,s[-1]=='d',uR)._repr_svg_()+"&nbsp; &nbsp; &nbsp; "
            elif t in x.relations.keys():
                st+=hasse_diagram(x.relations[t], True, s[-1]=='d',uR)._repr_svg_()+"&nbsp; &nbsp; &nbsp; "
        st+=" &nbsp; "
    display_html(st,raw=True)
