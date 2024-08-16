from core.utils import Utils
from requests import get

utils = Utils()

class Offsets:
    try:
        offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
        client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()
        button = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/buttons.json").json()

        dwEntityList = offset["client.dll"]["dwEntityList"]
        dwViewMatrix = offset["client.dll"]["dwViewMatrix"]
        dwLocalPlayerPawn = offset["client.dll"]["dwLocalPlayerPawn"]
        dwLocalPlayerController = offset["client.dll"]["dwLocalPlayerController"]
        dwViewAngles = offset["client.dll"]["dwViewAngles"]
        m_iszPlayerName = client["client.dll"]["classes"]["CBasePlayerController"]["fields"]["m_iszPlayerName"]
        m_iHealth = client["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iHealth"]
        m_iTeamNum = client["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iTeamNum"]
        m_vOldOrigin = client["client.dll"]["classes"]["C_BasePlayerPawn"]["fields"]["m_vOldOrigin"]
        m_pGameSceneNode = client["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_pGameSceneNode"]
        m_hPlayerPawn = client["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_hPlayerPawn"]
        m_iPing = client["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_iPing"]
        m_iScore = client["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_iScore"]
        m_ArmorValue = client["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_ArmorValue"]
        m_iPawnHealth = client["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_iPawnHealth"]
        m_iIDEntIndex = client["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_iIDEntIndex"]
        m_flFlashMaxAlpha = client["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashMaxAlpha"]
        m_iDesiredFOV = client["client.dll"]["classes"]["CBasePlayerController"]["fields"]["m_iDesiredFOV"]
        jump = button["client.dll"]["jump"]
        attack = button["client.dll"]["attack"]
    except:
        utils.ShowMessageBox("Error", "An error occurred while obtaining the offsets, please wait for an update", 0x10)
