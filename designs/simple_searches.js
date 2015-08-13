{
  "_id": "_design/simple",
  "_rev": "8-6a48cd1350c55ca61078dece73214426",
  "views": {
    "monsters": {
      "map": "function(doc) {\n\tif (doc.object_type == \"monster\") {\n\t\temit(doc._id, {\n\t\t\t_id: doc._id,\n\t\t\tname: doc.name\n\t\t});\n\t}\n}"
    },
    "weapons": {
      "map": "function(doc) {\n\tif (doc.object_type == \"weapon\") {\n\t\temit(doc._id, {\n\t\t\t_id: doc._id,\n\t\t\tname: doc.name\n\t\t});\n\t}\n}"
    },
    "armor": {
      "map": "function(doc) {\n\tif (doc.object_type == \"armor\") {\n\t\temit(doc._id, {\n\t\t\t_id: doc._id,\n\t\t\tname: doc.name\n\t\t});\n\t}\n}"
    },
    "items": {
      "map": "function(doc) {\n\tif (doc.object_type == \"item\") {\n\t\temit(doc._id, {\n\t\t\t_id: doc._id,\n\t\t\tname: doc.name\n\t\t});\n\t}\n}"
    },
    "objects": {
      "map": "function(doc) {\n\tif ([\"item\", \"armor\", \"weapon\", \"monster\"].indexOf(doc.object_type) >= 0) {\n\t\temit(doc.name, {\n\t\t\t_id: doc._id,\n\t\t\tname: doc.name\n\t\t});\n\t}\n}"
    }
  },
  "language": "javascript"
}