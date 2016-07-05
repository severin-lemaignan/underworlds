#include <system_error>

#include <boost/uuid/uuid_io.hpp>
#include <boost/uuid/uuid_generators.hpp>

#include "underworlds.pb.h"

#include "uwds.hpp"

using namespace std;
using namespace uwds;



Node::Node(std::shared_ptr<Scene> scene) : id(boost::uuids::to_string(boost::uuids::random_generator()())),
                                     _scene(scene) {};

Node::Node(const Node& n) : id(boost::uuids::to_string(boost::uuids::random_generator()())),
                      name(n.name),
                      type(n.type),
                      parent(n.parent),
                      children(n.children),
                      transform(n.transform),
                      last_update(n.last_update),
                      _scene(n._scene) {}



underworlds::Node Node::serialize() const {

    underworlds::Node node;
    node.set_id(id);
    node.set_name(name);
    node.set_type((underworlds::Node_NodeType) type);

    node.set_parent(parent);

    for (const auto& child : children) {
        node.add_children(child);
    }

    return node;
}


Node Node::deserialize(const underworlds::Node& remoteNode, shared_ptr<Scene> scene) {

    auto node = Node(scene);
    node.id = remoteNode.id();
    node.name = remoteNode.name();
    node.type = (NodeType) remoteNode.type();
    
    node.parent = remoteNode.parent();

    for(int i = 0; i < remoteNode.children_size(); i++) {
        node.children.insert(remoteNode.children(i));

    }


    return node;
}


std::ostream& operator<<(std::ostream& os, const uwds::Node& node)
{
    os << node.name << " [" << node.id << "]";
    return os;
}
