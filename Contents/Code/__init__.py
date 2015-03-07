MUSIC_PREFIX = "/music/nzradio"

NAME = L('Kiwi Radio')

ART = 'art-default.jpg'
ICON = 'icon-default.png'

import station_list as radio_station


def Start():
    '''
    The Start function is initially called by the PMS framework to initialize the plugin.
    This includes setting up the Plugin static instance along with the displayed artwork.
    '''
    Plugin.AddPrefixHandler(MUSIC_PREFIX, MusicMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    # Initialize the plugin
    # Plugin.AddViewGroup('the_view_group', viewMode='List', mediaType='items')

    # Setup the artwork associated with the plugin
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)
    
    HTTP.CacheTime = CACHE_1HOUR
    


# @handler(PREFIX, 'NZ Radio')
def MusicMainMenu():
    '''
    MainMenu populates the menu with the buttons that the user will use to select the station that they wish to listen to.
    '''

    oc = ObjectContainer()
    oc.add(CreateTrackObject(url=radio_station.national, title='National Radio', fmt='hls'))
    oc.add(CreateTrackObject(url=radio_station.concert, title='Concert FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.international, title='National Radio (International)', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.upoku, title='Te Upoko O Te Ika', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.hiku_ika, title='Te Hiku O Te Ika', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.moana, title='Moana', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.nga_iwi, title='Nga Iwi', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.pumanawa, title='Pumanawa', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.tainui, title='Tainui', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.turanga, title='Turanga', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.tuwharetoa, title='Tuwharetoa', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.waatea, title='Waatea', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.tautoko, title='Tautoko', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.ngati_porou, title='Ngati Porou', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.koimako, title='Korimako', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.kahungunu, title='Kahungunu', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.ngati_hene, title='Ngati Hene', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.awa, title='Awa', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.tahu, title='Tahu', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.atiawa_toa, title='Atiawa Toa', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.maniapoto, title='Maniapoto', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.sun, title='Sun', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.sunFM, title='Sun FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.kia_ora, title='Kia Ora', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.raukava, title='Raukava', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.the_breeze_auckland, title='The Breeze (Auckland)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.the_breeze_hamilton, title='The Breeze (Hamilton)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.the_breeze_wellington, title='The Breeze (Wellington)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.chch_breeze, title='The Breeze (Christchurch)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.manawatu_breeze, title='The Breeze (Manawatu)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.nelson_breeze, title='The Breeze (Nelson)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.george_fm, title='George FM', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.kiwi_fm, title='Kiwi FM', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.mai_fm, title='Mai FM', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_akl, title='More FM (Auckland)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_blenheim, title='More FM (Blenheim)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_chch, title='More FM (Christchurch)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_dunedin, title='More FM (Dunedin)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_hastings, title='More FM (Hastings)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_masterton, title='More FM (Masterton)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_nelson, title='More FM (Nelson)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_queenstown, title='More FM (Queenstown)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_southland, title='More FM (Southland)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_taupo, title='More FM (Taupo)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_tauranga, title='More FM (Tauranga)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_taranaki, title='More FM (Taranaki)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_wanganui, title='More FM (Wanganui)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_whangarei, title='More FM (Whangarei)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.more_fm_wellington, title='More FM (Wellington)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.radio_live, title='Radio Live', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.the_edge, title='The Edge', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.the_rock, title='The Rock', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.the_sound, title='The Sound', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.times_fm_orewa, title='Times FM (Orewa)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.radio_dunedin, title='Radio Dunedin', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.hits_akl, title='The Hits (Auckland)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.hits_chch, title='The Hits (Christchurch)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.hits_wgtn, title='The Hits (Wellington)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.coast_fm, title='Coast FM', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.radio_sport, title='Radio Sport', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.flava_online, title='Flava Online', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.hokonui_gore_fm, title='Hokonui Gold (Gore)', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.newstalk_zb, title='Newstalk ZB', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.radio_hauraki, title='Radio Hauraki', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.accessManawatu, title='Access Manawatu', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.botany, title='Botany Radio', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.coast_access, title='Coast Access Radio', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.coromandel_fm, title='Coromandel FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.fresh_fm, title='Fresh FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.free_fm, title='Free FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.the_flat, title='The Flat', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.howick_village_radio, title='Howick Village Radio', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.maranui_fm, title='Maranui FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.oddhosting, title='Oddhosting', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.plains_fm, title='Plains FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.pulzar_fm, title='Pulzar FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.radio_kidnappers, title='Radio Kidnappers', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.radio_reading_service, title='Radio Reading Service', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.radio_southland, title='Radio Southland', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.toroa_radio, title='Toroa Radio', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.wellington_radio, title='Wellington Radio', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.apna990am, title='APNA Radio', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.cool_blue, title='Cool Blue', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.radio1xx, title='Radio 1XX', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.cheeseFM, title='Cheese FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.baseFM, title='Base FM', fmt='aac'))
    # oc.add(CreateTrackObject(url=radio_station.country_radio, title='National Radio', fmt='mp3'))
    oc.add(CreateTrackObject(url=radio_station.fleet_fm, title='Fleet FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.kFM, title='K FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.niu_fm, title='NIU FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.pi_531, title='Pacific Islands 531', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.up_fm, title='UP FM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.bFM, title='bFM', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.radio_active, title='Radio Active', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.radio_one, title='Radio One', fmt='aac'))
    oc.add(CreateTrackObject(url=radio_station.static_fm, title='Static FM', fmt='aac'))
    
    return oc


def CreateTrackObject(url, title, fmt, include_container=False):
    '''
    CreateTrackObject creates
    Inputs:
    -------
        url - URL
            URL of stream

        title - String
            Title of the stream

        fmt - String
            Format of the stream

        include_container - boolean
            If true return the track_object inside an ObjectContainer
    Returns:
    -------
        TrackObject - Object containing Callback and Media Object

    '''
    # choose container and codec to use for the supplied format
    if fmt == 'mp3':
        container = Container.MP3
        audio_codec = AudioCodec.MP3
    elif fmt == 'aac':
        container = Container.MP4
        audio_codec = AudioCodec.AAC
    elif fmt == 'hls':
        protocol = 'hls'
        container = 'mpegts'
        # video_codec = VideoCodec.H264
        audio_codec = AudioCodec.AAC

    # create TrackObject for stream
    track_object = TrackObject(
        key=Callback(CreateTrackObject, url=url, title=title, fmt=fmt, include_container=True),
        rating_key=url,
        title=title,
        items=[
            MediaObject(
                parts=[
                    PartObject(key=Callback(PlayAudio, url=url, ext=fmt))
                ],
                container=container,
                audio_codec=audio_codec,
                audio_channels=2
            )
        ]
    )

    if include_container:
        return ObjectContainer(objects=[track_object])
    else:
        return track_object


def PlayAudio(url):
    '''
    PlayAudio
    Inputs:
    -------
        url - URL of stream
    '''
    return Redirect(url)
