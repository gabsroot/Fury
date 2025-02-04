from requests import get
import ctypes

try:
    offsets = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
    client_dll = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()

    dwEntityList = offsets["client.dll"]["dwEntityList"]
    dwViewMatrix = offsets["client.dll"]["dwViewMatrix"]
    dwLocalPlayerPawn = offsets["client.dll"]["dwLocalPlayerPawn"]
    dwLocalPlayerController = offsets["client.dll"]["dwLocalPlayerController"]
    dwViewAngles = offsets["client.dll"]["dwViewAngles"]
    m_iszPlayerName = client_dll["client.dll"]["classes"]["CBasePlayerController"]["fields"]["m_iszPlayerName"]
    m_iHealth = client_dll["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iHealth"]
    m_iTeamNum = client_dll["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iTeamNum"]
    m_vOldOrigin = client_dll["client.dll"]["classes"]["C_BasePlayerPawn"]["fields"]["m_vOldOrigin"]
    m_pGameSceneNode = client_dll["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_pGameSceneNode"]
    m_hPlayerPawn = client_dll["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_hPlayerPawn"]
    m_iPing = client_dll["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_iPing"]
    m_iScore = client_dll["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_iScore"]
    m_ArmorValue = client_dll["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_ArmorValue"]
    m_iPawnHealth = client_dll["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_iPawnHealth"]
    m_iIDEntIndex = client_dll["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_iIDEntIndex"]
    m_flFlashMaxAlpha = client_dll["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_flFlashMaxAlpha"]
    m_iDesiredFOV = client_dll["client.dll"]["classes"]["CBasePlayerController"]["fields"]["m_iDesiredFOV"]
    m_aimPunchAngle = client_dll["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_aimPunchAngle"]
    m_entitySpottedState = client_dll["client.dll"]["classes"]["C_CSPlayerPawn"]["fields"]["m_entitySpottedState"]
    m_bSpotted = client_dll["client.dll"]["classes"]["EntitySpottedState_t"]["fields"]["m_bSpotted"]
    m_pClippingWeapon = client_dll["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_pClippingWeapon"]
    m_AttributeManager = client_dll["client.dll"]["classes"]["C_EconEntity"]["fields"]["m_AttributeManager"]
    m_Item = client_dll["client.dll"]["classes"]["C_AttributeContainer"]["fields"]["m_Item"]
    m_iItemDefinitionIndex = client_dll["client.dll"]["classes"]["C_EconItemView"]["fields"]["m_iItemDefinitionIndex"]
    m_pBoneArray = client_dll["client.dll"]["classes"]["CSkeletonInstance"]["fields"]["m_modelState"] + 128
except:
    ctypes.windll.user32.MessageBoxW(0, "Failed to get offsets.", "Error", 0x10)
