#include<stdio.h>

int graph[1001][1001];
int visited[1001];

void dfs(int start, int n) {
	visited[start] = 1;
	for (int i = 1; i <= n; i++) {
		if (graph[start][i] == 1 && !visited[i]) {
			dfs(i, n);
		}
	}
}

int main() {

	int n, m, cnt = 0;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < m; i++) {
		int u, v;
		scanf("%d %d", &u, &v);
		graph[u][v] = 1;
		graph[v][u] = 1;
	}

	for (int i = 1; i <= n; i++) {
		if (!visited[i]) {
			cnt++;
			dfs(i, n);
		}
	}

	printf("%d", cnt);

	return 0;
}