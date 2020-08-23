def parse_results(req):
    if req is None:
        return {'fulfillmentText': "Not a valid request"}
    else:
        action_name = req.get('queryResult').get('action')
        parameters = req.get('queryResult').get('parameters')
        query = req.get('queryResult').get('queryText')
        output_context_list = req.get('queryResult').get('outputContexts')
        params_dict = parse_output_context_list(output_context_list)
        print(params_dict)
        print("#"*20)
        if "save_user_name" in action_name:
            given_name = params_dict["given-name"]
            return {'fulfillmentText': "Thank you {0}. Please provide your email so that "
                                       "we can connect better".format(given_name)}
        elif "save_email" in action_name:
            email_address = params_dict["email_address"]
            given_name = params_dict["given-name"]
            return {'fulfillmentText': "Thank you {0}. Your email is recorded as {1}. "
                                       "Please help us with your phone number".format(given_name, email_address)}
        elif "save_phone" in action_name:
            phone_number = params_dict["phone-number"]
            given_name = params_dict["given-name"]
            email_address = params_dict["email_address"]
            return {'fulfillmentText': "Thank you {0}. Your email is recorded as {1} and phone number is {2}. "
                                       "What is problem you are facing?".format(given_name, email_address,
                                                                                phone_number)}
        elif "save_case" in action_name:
            phone_number = params_dict["phone_number"]
            given_name = params_dict["given-name"]
            email_address = params_dict["email_address"]
            case_provided = params_dict["case"]
            return {'fulfillmentText': "Thank you {0}. Your email is recorded as {1} and phone number is {2}. "
                                       "Your case is '{3}', our team will reach out to you. "
                                       "Do you have any supporting documents?".format(given_name, email_address,
                                                                                      phone_number, case_provided)}


def parse_output_context_list(output_context_list):
    final_params = {}
    if not len(output_context_list) == 0:
        for each_opt_cntxt in output_context_list:
            parameter_dict = dict(each_opt_cntxt["parameters"])
            parameter_dict_keys = parameter_dict.keys()
            for each_param_dict_key in parameter_dict_keys:
                value = str(parameter_dict[each_param_dict_key])
                if not each_param_dict_key in final_params.keys():
                    if not len(value) == 0:
                        final_params[each_param_dict_key] = value

    return final_params
