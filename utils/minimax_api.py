import json
import requests
import base64
from pathlib import Path
from typing import Dict, Any, Optional, List
import time

class MiniMaxAPI:
    def __init__(self, config_path: str = "config/minimax_config.json"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        self.base_url = self.config['api']['base_url']
        self.api_key = self.config['api']['api_key']
        self.group_id = self.config['api']['group_id']
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def text_to_speech(
        self,
        text: str,
        voice_id: str = "female-sweet",
        output_path: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Convierte texto a voz usando la API de MiniMax
        
        Args:
            text: Texto a convertir
            voice_id: ID de la voz a usar
            output_path: Ruta donde guardar el audio generado
            **kwargs: Parámetros adicionales (speed, vol, pitch, emotion)
        
        Returns:
            Dict con información sobre el audio generado
        """
        endpoint = f"{self.base_url}/v1/tts"
        
        # Obtener configuración de voz predeterminada
        voice_config = self.config['tts']['voices'].get(
            voice_id, 
            {"voice_id": voice_id, "voice_setting": self.config['tts']['default_settings']['voice_setting']}
        )
        
        # Actualizar con parámetros personalizados
        voice_setting = voice_config['voice_setting'].copy()
        for key in ['speed', 'vol', 'pitch', 'emotion']:
            if key in kwargs:
                voice_setting[key] = kwargs[key]
        
        payload = {
            "model": self.config['tts']['default_settings']['model'],
            "text": text,
            "group_id": self.group_id,
            "voice_id": voice_config.get('voice_id', voice_id),
            "voice_setting": voice_setting,
            "format": kwargs.get('format', self.config['tts']['default_settings']['format'])
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get('base_resp', {}).get('status_code') == 0:
                # Decodificar y guardar el audio
                audio_data = base64.b64decode(result['audio'])
                
                if output_path:
                    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(audio_data)
                
                return {
                    "success": True,
                    "output_path": output_path,
                    "trace_id": result.get('trace_id'),
                    "audio_size": len(audio_data),
                    "format": payload['format']
                }
            else:
                return {
                    "success": False,
                    "error": result.get('base_resp', {}).get('status_msg', 'Unknown error')
                }
                
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": f"Request failed: {str(e)}"
            }
    
    def generate_audio_segments(
        self,
        segments: List[Dict[str, Any]],
        output_dir: str
    ) -> List[Dict[str, Any]]:
        """
        Genera múltiples segmentos de audio
        
        Args:
            segments: Lista de segmentos con texto y configuración
            output_dir: Directorio donde guardar los audios
        
        Returns:
            Lista con información de cada segmento generado
        """
        results = []
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        for i, segment in enumerate(segments):
            segment_id = segment.get('id', f"{i+1:03d}")
            speaker = segment.get('speaker', 'default')
            text = segment['text']
            
            # Mapear nombres de locutores a voice_ids
            voice_mapping = {
                'María': 'maria',
                'maria': 'maria',
                'Carlos': 'carlos',
                'carlos': 'carlos'
            }
            
            voice_id = voice_mapping.get(speaker, 'female-sweet')
            
            # Configuración específica del segmento
            voice_settings = segment.get('voice_settings', {})
            
            output_file = f"{output_dir}/{speaker.lower()}_{segment_id}.mp3"
            
            print(f"Generando segmento {segment_id} - {speaker}: {text[:50]}...")
            
            result = self.text_to_speech(
                text=text,
                voice_id=voice_id,
                output_path=output_file,
                **voice_settings
            )
            
            if result['success']:
                segment_result = {
                    "id": segment_id,
                    "speaker": speaker,
                    "text": text,
                    "audio_file": output_file,
                    "status": "success"
                }
            else:
                segment_result = {
                    "id": segment_id,
                    "speaker": speaker,
                    "text": text,
                    "status": "failed",
                    "error": result['error']
                }
            
            results.append(segment_result)
            
            # Pausa entre llamadas para evitar rate limiting
            time.sleep(0.5)
        
        return results
    
    def generate_music(
        self,
        prompt: str,
        duration: int = 10,
        output_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Genera música de fondo usando la API de MiniMax
        
        Args:
            prompt: Descripción de la música deseada
            duration: Duración en segundos
            output_path: Ruta donde guardar el audio
        
        Returns:
            Dict con información sobre la música generada
        """
        endpoint = f"{self.base_url}/v1/audio/generation"
        
        payload = {
            "model": self.config['audio']['default_settings']['model'],
            "prompt": prompt,
            "duration": duration,
            "group_id": self.group_id
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get('base_resp', {}).get('status_code') == 0:
                audio_data = base64.b64decode(result['audio'])
                
                if output_path:
                    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(audio_data)
                
                return {
                    "success": True,
                    "output_path": output_path,
                    "trace_id": result.get('trace_id')
                }
            else:
                return {
                    "success": False,
                    "error": result.get('base_resp', {}).get('status_msg', 'Unknown error')
                }
                
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": f"Request failed: {str(e)}"
            }

# Funciones de utilidad para uso directo
def generate_podcast_audio(script_path: str, output_dir: str) -> Dict[str, Any]:
    """
    Genera audio completo de un podcast desde un guión
    
    Args:
        script_path: Ruta al archivo del guión
        output_dir: Directorio de salida
    
    Returns:
        Dict con información del proceso
    """
    api = MiniMaxAPI()
    
    # Leer y parsear el guión
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer segmentos del guión
    segments = parse_script_segments(content)
    
    # Generar audio para cada segmento
    results = api.generate_audio_segments(segments, output_dir)
    
    # Guardar metadata
    metadata_path = f"{output_dir}/generation_metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump({
            "script_path": script_path,
            "total_segments": len(segments),
            "successful": sum(1 for r in results if r.get('status') == 'success'),
            "failed": sum(1 for r in results if r.get('status') == 'failed'),
            "segments": results
        }, f, indent=2, ensure_ascii=False)
    
    return {
        "success": True,
        "metadata_path": metadata_path,
        "results": results
    }

def parse_script_segments(content: str) -> List[Dict[str, Any]]:
    """
    Parsea un guión para extraer segmentos de audio
    
    Args:
        content: Contenido del guión
    
    Returns:
        Lista de segmentos con texto y configuración
    """
    segments = []
    lines = content.split('\n')
    
    current_segment = None
    segment_id = 1
    
    for line in lines:
        line = line.strip()
        
        # Detectar líneas de locutor
        if line.startswith('**María:**') or line.startswith('**Carlos:**'):
            if current_segment:
                segments.append(current_segment)
            
            speaker = 'María' if 'María' in line else 'Carlos'
            text = line.split(':', 1)[1].strip() if ':' in line else ''
            
            current_segment = {
                'id': f"{segment_id:03d}",
                'speaker': speaker,
                'text': text
            }
            segment_id += 1
        
        # Agregar texto adicional al segmento actual
        elif current_segment and line and not line.startswith('*') and not line.startswith('#'):
            current_segment['text'] += ' ' + line
    
    # Agregar último segmento
    if current_segment:
        segments.append(current_segment)
    
    return segments

if __name__ == "__main__":
    # Ejemplo de uso
    api = MiniMaxAPI()
    
    # Probar TTS
    result = api.text_to_speech(
        text="Hola, esta es una prueba de la API de MiniMax",
        voice_id="maria",
        output_path="test_audio.mp3"
    )
    
    print(json.dumps(result, indent=2))