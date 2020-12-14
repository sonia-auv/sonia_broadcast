# Sonia Broadcast
This project is used to broadcast the data from ROS to UDP. This broadcast is running on the SONIA Dockbox.

## Getting Started


### Add a new subscriber

To add a new subscriber, you simply have to add a new entry in the subscriber_list in this file. (subscribers/subscribers_list.py)

Example: `sub_list.append(Subscriber(ros_connector, '/topic_name', 'topic_type'))`

### Installing

Add installation notes...

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details
