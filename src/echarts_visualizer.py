def get_smart_label(item, index, parent_key):
    """
    :param data: item in a list
    :return: string label

    Reads and finds  human-readable label for an item in a list
    based on parent_key [i.e. the seciton of the file ] we are in.
    """
    if not isinstance(item, dict):
        return f"[{index}]"

    # --- 1. DISEASES ---
    if "diseases" in str(parent_key).lower():
        if "term" in item and "label" in item["term"]:
            return item["term"]["label"]

    # --- 2. PHENOTYPIC FEATURES ---
    if "phenotypic" in str(parent_key).lower():
        if "type" in item and "label" in item["type"]:
            return item["type"]["label"]

    # --- 3. GENOMIC INTERPRETATIONS ---
    if "genomic" in str(parent_key).lower():
        # Case A: It's a Gene
        if "geneDescriptor" in item and "symbol" in item["geneDescriptor"]:
            return f"Gene: {item['geneDescriptor']['symbol']}"

        # Case B: It's a Variant
        if "variantInterpretation" in item:
            vi = item["variantInterpretation"]
            if "variationDescriptor" in vi and "label" in vi["variationDescriptor"]:
                return f"Variant: {vi['variationDescriptor']['label']}"
            if "variationDescriptor" in vi and "id" in vi["variationDescriptor"]:
                return f"Variant: {vi['variationDescriptor']['id']}"

    # --- 4. INTERPRETATIONS (Top Level) ---
    if "interpretations" in str(parent_key).lower():
        if "diagnosis" in item and "disease" in item["diagnosis"]:
            d_label = item["diagnosis"]["disease"].get("label")
            if d_label:
                return f"Diagnosis: {d_label}"
        if "id" in item:
            return f"Interpretation: {item['id']}"

    # --- FALLBACKS (If nothing specific matched) ---
    if "label" in item:
        return item["label"]
    if "id" in item:
        return item["id"]
    if "name" in item:
        return item["name"]

    # If all else fails, return the number
    return f"[{index}]"


def parse_to_echarts(data, label="Root", parent_key=""):
    """
    :param data: data file
    :return: i.e. flat tree data structure

    Recursive parser that builds the ECharts JSON.
    Handles Smart Labeling, Coloring, and Flattening.
    """

    # --- COLOR LOGIC  ---
    node_color = "#5470c6"  # Default Blue for structural nodes (Patient, Subject, etc.)

    # A. Check for 'excluded: true' (Red)
    if isinstance(data, dict) and data.get("excluded") is True:
        node_color = "#FF6B6B"  # Red

    # B. Check Context (Green/Pink/Blue) - Priority 2
    elif "phenotypic" in str(parent_key).lower():
        node_color = "#91CC75"  # Green (Observed Features)

    # Create the Node Structure
    node = {
        "name": str(label),
        "itemStyle": {
            "color": node_color,
            "borderColor": node_color
        },
        "children": []
    }

    # Handle Dictionary
    if isinstance(data, dict):
        for key, value in data.items():

            node_color = '#FF6B6B' if 'exluded' in str(key).lower() else '#91CC75'

            # --- FLATTENING LOGIC (Skip 'type' and 'term' wrappers) ---
            if key in ["type", "term"] and isinstance(value, dict):
                # Try to grab the Label directly
                display_text = value.get("id", value.get("label"))
                if display_text:
                    # Append direct child
                    node["children"].append({
                        "name": display_text,
                        "itemStyle": {"color": node_color, "borderColor": node_color}
                    })
                    continue  # Skip normal recursion for this key

            # NORMAL RECURSION
            if isinstance(value, (str, int, float, bool)):
                # Leaf node
                node["children"].append({
                    "name": f"{key}: {value}",
                    "itemStyle": {"color": "#ccc", "borderColor": "#ccc"}
                })
            else:
                # Recurse down, passing 'key' as the new parent context
                node["children"].append(parse_to_echarts(value, label=key, parent_key=key))

    # 4. Handle List
    elif isinstance(data, list):
        for i, item in enumerate(data):
            # Pass parent_key so labeler knows we are in 'Diseases' etc.
            smart_name = get_smart_label(item, i, parent_key=label)

            # Pass 'label' as the parent_key for the next level
            child = parse_to_echarts(item, label=smart_name, parent_key=label)
            node["children"].append(child)

    # 5. Handle Primitive Value
    else:
        node["name"] = f"{label}: {data}"

    return node
