import graphviz


def create_topology_graph(data):
    '''

    :param data: dictionary
    :return: graphviz graph
    '''
    graph = graphviz.Digraph()
    # Defining attributes
    graph.attr(rankdir='LR')
    graph.attr('node', shape='box', style='filled', color='lightblue')
    graph.attr(ranksep='1.5', nodesep='1.0')
    graph.attr('node', fontsize='14', fontname="Helvetica")
    graph.attr(splines='polyline')

    def add_nodes(parent_name, current_data):
        '''

        :param parent_name:
        :param current_name:
        :return:
        '''
        if isinstance(current_data, dict):
            for key, value in current_data.items():
                node_id = f'{parent_name}_{key}'

                if isinstance(value, list):
                    if len(value) < 2:
                        # Draw the Category Node
                        graph.node(node_id, key)
                        graph.edge(parent_name, node_id)

                        for i, item in enumerate(value):
                            # Create ID
                            item_id = f'{node_id}_{i}'

                            if isinstance(item, dict):
                                graph.node(item_id, f"#{i + 1}", shape="point", width="0.1")  # Tiny dot
                                graph.edge(node_id, item_id, arrowsize="0.5")
                                add_nodes(item_id, item)

                            else:
                                # Direct connection to value
                                leaf_id = f'{item_id}_value'
                                graph.node(leaf_id, str(item), shape='plain')  # 'plain' removes the box
                                graph.edge(node_id, leaf_id)
                    else:
                        # CASE B: Large List -> SUMMARIZE
                        label = f"{key}\n[{len(value)} items]"
                        graph.node(node_id, label, fillcolor='#ffcccc')
                        graph.edge(parent_name, node_id)

                elif isinstance(value, dict):
                    graph.node(node_id, key)
                    graph.edge(parent_name, node_id)
                    add_nodes(node_id, value)

                else:
                    leaf_id = f'{node_id}_val'
                    graph.node(node_id, key)
                    graph.node(leaf_id, str(value), shape='ellipse', fillcolor='lightyellow')
                    graph.edge(parent_name, node_id)
                    graph.edge(node_id, leaf_id)

    graph.node('Root', 'Phenopacket')
    add_nodes('Root', data)

    return graph
