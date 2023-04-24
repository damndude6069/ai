#include <iostream>
#include <queue>
#define SIZE 5
using namespace std;
char vertices[SIZE] = {'B', 'A', 'E', 'D', 'C'};
int visited[SIZE] = {0};
int adjacencyM[SIZE][SIZE] = {{0, 1, 1, 0, 0},
			      {1, 0, 0, 1, 0},
			      {1, 0, 0, 0, 1},
			      {0, 1, 0 ,0, 0},
			      {0, 1, 1, 0, 0}
			      };
class BREADTHFIRSTSEARCH{
	public:
	void solve(int root){
		queue<int> Queue;
		visited[root] = 1;
		Queue.push(root);
		while(!Queue.empty()){
			int current_vertex= Queue.front();
			Queue.pop();
			cout << vertices[current_vertex] << " ";
			int neighbor_Vertex;
			while((neighbor_Vertex =unvisitedNeighbor(current_vertex)) != -1){
				visited[neighbor_Vertex] = 1;
				Queue.push(neighbor_Vertex);
			}
		}
	}
	int unvisitedNeighbor(int index){
		for(int i=0; i<SIZE; i++){
			if(adjacencyM[index][i] == 1 && (visited[i] == 0)){
				return i;
			}
		}
		return -1;
	}
};
int main() {
	BREADTHFIRSTSEARCH bfs;
	bfs.solve(0);
	return 0;
}