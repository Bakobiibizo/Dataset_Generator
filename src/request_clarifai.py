import os
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


def run_clarifai(
    workflow_id: Optional[str] = "cohere-summarize-workflow-88z5zr",
    text_file_url: Optional[
        str
    ] = "https://samples.clarifai.com/negative_sentence_12.txt",
):
    pat = os.getenv("PAT")
    user_id = os.getenv("USER_ID")
    app_id = os.getenv("APP_ID")
    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (("authorization", f"Key {pat}"),)

    userDataObject = resources_pb2.UserAppIDSet(user_id, app_id)

    post_workflow_results_response = stub.PostWorkflowResults(
        service_pb2.PostWorkflowResultsRequest(
            user_app_id=userDataObject,
            workflow_id=workflow_id,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(text=resources_pb2.Text(url=text_file_url))
                )
            ],
        ),
        metadata=metadata,
    )
    if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
        print(post_workflow_results_response.status)
        raise ConnectionError(
            "Post workflow results failed, status: "
            + post_workflow_results_response.status.description
        )

    # We'll get one WorkflowResult for each input we used above. Because of one input, we have here one WorkflowResult
    results = post_workflow_results_response.results[0]

    # Each model we have in the workflow will produce one output.
    for output in results.outputs:
        model = output.model

        print("Predicted concepts for the model `%s`" % model.id)
        for concept in output.data.concepts:
            print("	%s %.2f" % (concept.name, concept.value))

    # Uncomment this line to print the full Response JSON
    # print(results)
