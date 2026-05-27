output "ip" {
  value = google_compute_network.vpc_network.name
}

output "cluster" {
  value = google_container_cluster.clustertestapp.name
}

output "node" {
  value = google_container_node_pool.primary_nodes.name
}