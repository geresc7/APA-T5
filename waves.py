import struct as st

def abrewave(fichero):
    with open(fichero, "rb") as fpwave:
        cabecera = "< 4s "
        buffer = fpwave.read(st.calcsize(cabecera))
        chunkID, chunksize, format = st.unpack(cabecera, buffer)
        if chunkID != b"RIFF" or format =! b"WAVE":
            raise Exception("Fichero no es wave") from None

        cabecera = "<4si2H"
        buffer = fpwave.read(st.calcsize(cabecera))
        (subchunk1ID, subchunk1size, audioformat, 
        numchannels, samplerate, bitrate, 
        blockalign, bitspersample) = st.unpack(cabecera, buffer)

        
    return  chunkID, chunksize, format + (subchunk1ID, subchunk1size, audioformat, 
        numchannels, samplerate, bitrate, 
        blockalign, bitspersample)