from js import handTrack, setTimeout, requestAnimationFrame, player
from pyodide import create_once_callable
import asyncio

context = canvas.element.getContext("2d")

isVideo = False
model = None
last_position = 0
direction = "stop"

modelParams = {
    "flipHorizontal": True,  # flip e.g for video
    "maxNumBoxes": 20,  # maximum number of boxes to detect
    "iouThreshold": 0.5,  # ioU threshold for non-max suppression
    "scoreThreshold": 0.6,  # confidence threshold for predictions.
}


def toggle_video(evt):
    global isVideo
    player.jump()

    if (not isVideo):
        update_note.write("Starting video")
        pyscript.run_until_complete(start_video())
    else:
        update_note.write("Stopping video")
        handTrack.stopVideo(video.element)
        isVideo = False
        update_note.write("Video stopped")


async def start_video():
    global isVideo
    update_note.write("Inside start video")
    status = await handTrack.startVideo(video.element)
    console.log("video started", status)
    if status:
        update_note.write("Video started. Now tracking")
        isVideo = True
        console.log("Calling RUN DETECTION")
        y = await run_detection()
    else:
        update_note.write("Please enable video")


def sync_run_detection(evt):
    pyscript.run_until_complete(run_detection())


async def run_detection():
    global model
    global isVideo
    global last_position
    global direction

    predictions = await model.detect(video.element)
    model.renderPredictions(predictions, canvas.element,
                            context, video.element)

    if predictions:
        curr_position = predictions[0].bbox[0] + (predictions[0].bbox[2] / 2)
        delta = last_position - curr_position
        last_position = curr_position
        #console.log(delta, curr_position, last_position)
        if abs(delta) < 2:
            direction = "stop"
        elif delta > 0:
            direction = "left"
        else:
            direction = "right"

        for prediction in predictions:
            if prediction.label == 'open':
                player.jump()
            elif prediction.label == 'close':
                player.crouch()

    if (isVideo):
        await requestAnimationFrame(create_once_callable(sync_run_detection))


def handle_model(lmodel):
    global model
    model = lmodel
    update_note.write("Loaded Model!")


async def start():
    model = await handTrack.load(modelParams)  # .then(handle_model)
    handle_model(model)

pyscript.run_until_complete(start())
