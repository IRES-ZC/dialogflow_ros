#!/usr/bin/env python
import rospy
#from std_srvs.srv import Trigger
from nour_behave.srv import ServiceExample
def print_context_parameters(contexts):
    result = []
    for context in contexts:
        param_list = []
        temp_str = '\n\t'
        for parameter in context.parameters:
            param_list.append("{}: {}".format(
                    parameter, context.parameters[parameter]))
        temp_str += "Name: {}\n\tParameters:\n\t {}".format(
                context.name.split('/')[-1], "\n\t".join(param_list))
        result.append(temp_str)
    result = "\n".join(result)
    return result


def print_parameters(parameters):
    param_list = []
    temp_str = '\n\t'
    for parameter in parameters:
        param_list.append("{}: {}\n\t".format(
                parameter, parameters[parameter]))
        temp_str += "{}".format("\n\t".join(param_list))
        return temp_str

# Extract the plain parameter for the address
def getAddress(parameters):
    temp_str = ''
    for parameter in parameters:
        temp_str += "{}".format(parameters[parameter])
        return temp_str

def print_result(result):
    output = "DF_CLIENT: Results:\n" \
             "Query Text: {}\n" \
             "Detected intent: {} (Confidence: {})\n" \
             "Contexts: {}\n" \
             "Fulfillment text: {}\n" \
             "Action: {}\n" \
             "Parameters: {}".format(
                     result.query_text,
                     result.intent.display_name,
                     result.intent_detection_confidence,
                     print_context_parameters(result.output_contexts),
                     result.fulfillment_text,
                     result.action,
                     print_parameters(result.parameters))
    return output

#Check actions at each response
def checkAction(result):
    
    if result.action == 'map.navi':
        #rospy.init_node('service_server') 
        #rospy.wait_for_service('/move_robot')
        try:
            srv= rospy.ServiceProxy('/nour_naviagte', ServiceExample)
            serviceRes= srv(getAddress(result.parameters))
            print("{} service called...".format(result.action))
            print("Service Response:")
            print(serviceRes)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

    elif result.action == 'MoveCommand':
        #rospy.init_node('service_server') 
        #rospy.wait_for_service('/move_robot')
        try:
            srv= rospy.ServiceProxy('/nour_naviagte', ServiceExample)
            serviceRes= srv(getAddress(result.parameters))
            print("{} service called...".format(result.action))
            print("Service Response:")
            print(serviceRes)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
    else:
        print("No movement actions to take.")
        
    
