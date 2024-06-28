import time
import threading

from lib.comm.vision import ProtoVision
from lib.core.data import EntityData, FieldData
from lib.comm.control import ProtoControl
from lib.geometry.geometry import Geometry

from lib.helpers.configuration_helper import ConfigurationHelper
from lib.motion.motion import Motion
from lib.helpers.field_helper import FieldHelper
from lib.helpers.firasim_helper import FIRASimHelper

CONFIGURATION = ConfigurationHelper.getConfiguration()
    
IS_YELLOW_TEAM = CONFIGURATION["team"]["is-yellow-team"]
IS_YELLOW_LEFT_TEAM = CONFIGURATION["team"]["is-yellow-left-team"]

RUN_BOTH_TEAMS = True

IS_LEFT_TEAM = FieldHelper.isLeftTeam(IS_YELLOW_TEAM, IS_YELLOW_LEFT_TEAM)

CONTROL_IP = CONFIGURATION["FIRASim"]["control"]["ip"]
CONTROL_PORT = CONFIGURATION["FIRASim"]["control"]["port"]

GOAL_WIDTH = CONFIGURATION["field"]["goal"]["width"]
FIELD_LENGTH = CONFIGURATION["field"]["length"]

GOAL_LINE_DISTANCE_TO_CENTER = 0.7
DEFENSE_LINE_DISTANCE_TO_GOAL = 0.3

ATACKER_ROBOT_ID = 0
DEFENSE_ROBOT_ID = 1
GOALKEEPER_ROBOT_ID = 2


def followBall(
    fieldData: FieldData,
    vision: ProtoVision,
):
    ball = fieldData.ball

    counter = 0
    maxCounter = 100

    vision.update()
    
    while counter < maxCounter:

        vision.update()
        print(ball.position.x)
        print(ball.position.y)
        counter += 1
    
def main():
    fieldData = FieldData()
    vision = ProtoVision(
    team_color_yellow= IS_YELLOW_TEAM,
    field_data=fieldData)
    followBall(fieldData, vision)
if __name__ == '__main__':
    main()