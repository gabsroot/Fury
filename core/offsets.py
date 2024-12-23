from requests import get
import ctypes

try:
    offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
    client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()

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
    m_aimPunchAngle = client["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_aimPunchAngle"]
    m_entitySpottedState = client["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_entitySpottedState"]
    m_bSpotted = client["client.dll"]["classes"]["EntitySpottedState_t"]["fields"]["m_bSpotted"]
    m_pClippingWeapon = client["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_pClippingWeapon"]
    m_AttributeManager = client["client.dll"]["classes"]["C_EconEntity"]["fields"]["m_AttributeManager"]
    m_Item = client["client.dll"]["classes"]["C_AttributeContainer"]["fields"]["m_Item"]
    m_iItemDefinitionIndex = client["client.dll"]["classes"]["C_EconItemView"]["fields"]["m_iItemDefinitionIndex"]
    m_pBoneArray = client["client.dll"]["classes"]["CSkeletonInstance"]["fields"]["m_modelState"] + 128
except:
    ctypes.windll.user32.MessageBoxW(0, "Failed to get offsets, please wait for an update.", "Error", 0x10)
