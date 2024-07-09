from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {
            "role": "system",
            "content": "You are a professional StarCraft 2 player, skilled in analysing game strategies and match turning points.",
        },
        {
            "role": "user",
            "content": """
            
           00:12	Player 2 - Maru (Terran) - Unit born SCV [3880001]
00:12	Player 1 - Oliveira (Terran) - Unit born SCV [38C0001]
00:15	Player 2 - Maru (Terran) - Unit initiated SupplyDepot [3900001]
00:17	Player 1 - Oliveira (Terran) - Unit initiated SupplyDepot [3940001]
00:24	Player 1 - Oliveira (Terran) - Unit born SCV [3980001]
00:29	Player 2 - Maru (Terran) - Unit born SCV [39C0001]
00:36	Player 1 - Oliveira (Terran) - Unit born SCV [3A00001]
00:37	Player 2 - Maru (Terran) - Unit SupplyDepot [3900001] done
00:37	Player 2 - Maru (Terran) - Unit initiated BarracksFlying [3A40001]
00:38	Player 1 - Oliveira (Terran) - Unit SupplyDepot [3940001] done
00:39	Player 1 - Oliveira (Terran) - Unit initiated Barracks [3A80001]
00:41	Player 2 - Maru (Terran) - Unit initiated Refinery [3AC0001]
00:43	Player 1 - Oliveira (Terran) - Unit initiated Refinery [3B00001]
00:50	Player 1 - Oliveira (Terran) - Unit born SCV [3B40001]
00:53	Player 2 - Maru (Terran) - Unit initiated Barracks [3B80001]
00:55	Player 1 - Oliveira (Terran) - Unit initiated Refinery [3BC0001]
01:02	Player 2 - Maru (Terran) - Unit Refinery [3AC0001] done
01:02	Player 1 - Oliveira (Terran) - Unit born SCV [3C00001]
01:05	Player 1 - Oliveira (Terran) - Unit Refinery [3B00001] done
01:10	Player 2 - Maru (Terran) - Unit born SCV [3C40001]
01:15	Player 1 - Oliveira (Terran) - Unit born SCV [3C80001]
01:16	Player 1 - Oliveira (Terran) - Unit Refinery [3BC0001] done
01:22	Player 2 - Maru (Terran) - Unit born SCV [3CC0001]
01:23	Player 2 - Maru (Terran) - Unit BarracksFlying [3A40001] done
01:25	Player 1 - Oliveira (Terran) - Unit Barracks [3A80001] done
01:25	Player 1 - Oliveira (Terran) - Unit initiated BarracksReactor [3D00001]
01:26	Player 1 - Oliveira (Terran) - Unit born SCV [3D40001]
01:27	Player 1 - Oliveira (Terran) - Unit initiated SupplyDepotLowered [3D80001]
01:30	Player 2 - Maru (Terran) - Unit initiated Refinery [3DC0001]
01:40	Player 2 - Maru (Terran) - Unit Barracks [3B80001] done
01:42	Player 1 - Oliveira (Terran) - Unit initiated Factory [3E00001]
01:49	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3D80001] done
01:49	Player 2 - Maru (Terran) - Unit born MULE [3E40001]
01:49	Player 2 - Maru (Terran) - Unit OrbitalCommand [3540001] type changed to OrbitalCommand
01:51	Player 1 - Oliveira (Terran) - Unit OrbitalCommand [3200001] type changed to OrbitalCommand
01:52	Player 2 - Maru (Terran) - Unit Refinery [3DC0001] done
01:52	Player 1 - Oliveira (Terran) - Unit born MULE [3E80001]
01:54	Player 2 - Maru (Terran) - Unit initiated SupplyDepot [3EC0001]
01:57	Player 2 - Maru (Terran) - Unit born Reaper [3F00001]
01:57	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3D80001] type changed to SupplyDepotLowered
01:59	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3D80001] type changed to SupplyDepot
02:01	Player 1 - Oliveira (Terran) - Unit BarracksReactor [3D00001] done
02:01	Player 2 - Maru (Terran) - Unit born SCV [3F40001]
02:02	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3D80001] type changed to SupplyDepotLowered
02:02	Player 1 - Oliveira (Terran) - Unit SupplyDepot [3940001] type changed to SupplyDepotLowered
02:04	Player 1 - Oliveira (Terran) - Unit born SCV [3F80001]
02:13	Player 2 - Maru (Terran) - Unit born SCV [3FC0001]
02:14	Player 2 - Maru (Terran) - Unit born Reaper [4000001]
02:15	Player 2 - Maru (Terran) - Unit SupplyDepot [3EC0001] done
02:16	Player 1 - Oliveira (Terran) - Unit born SCV [4040001]
02:21	Player 1 - Oliveira (Terran) - Unit initiated OrbitalCommand [4080003]
02:21	Player 1 - Oliveira (Terran) - SprayTerran upgrade completed
02:25	Player 1 - Oliveira (Terran) - Unit Factory [3E00001] done
02:25	Player 2 - Maru (Terran) - Unit born SCV [40C0001]
02:26	Player 1 - Oliveira (Terran) - Unit died SCV [3980001].
02:27	Player 2 - Maru (Terran) - Unit initiated Factory [3980002]
02:28	Player 1 - Oliveira (Terran) - Unit born SCV [4100001]
02:29	Player 1 - Oliveira (Terran) - Unit died SCV [33C0001].
02:31	Player 2 - Maru (Terran) - Unit born Reaper [33C0002]
02:32	Player 1 - Oliveira (Terran) - Unit died SCV [3F80001].
02:34	Player 1 - Oliveira (Terran) - Unit born Reaper [3F80002]
02:37	Player 2 - Maru (Terran) - Unit born SCV [4140002]
02:38	Player 1 - Oliveira (Terran) - Unit born Reaper [4180001]
02:40	Player 2 - Maru (Terran) - Unit born KD8Charge [41C0001]
02:41	Player 1 - Oliveira (Terran) - Unit born SCV [3C80002]
02:41	Player 2 - Maru (Terran) - Unit born KD8Charge [41C0002]
02:41	Player 1 - Oliveira (Terran) - Unit died SCV [3C80001].
02:41	Player 2 - Maru (Terran) - Unit died KD8Charge [41C0001].
02:42	Player 1 - Oliveira (Terran) - Unit born KD8Charge [4200003]
02:42	Player 1 - Oliveira (Terran) - Unit died SCV [3440001].
02:42	Player 2 - Maru (Terran) - Unit died KD8Charge [41C0002].
02:44	Player 1 - Oliveira (Terran) - Unit died KD8Charge [4200003].
02:46	Player 2 - Maru (Terran) - Unit born Reaper [3440002]
02:48	Player 1 - Oliveira (Terran) - Unit born Hellion [41C0003]
02:50	Player 2 - Maru (Terran) - Unit born SCV [3A00002]
02:50	Player 2 - Maru (Terran) - Unit born KD8Charge [4200004]
02:50	Player 1 - Oliveira (Terran) - Unit died SCV [3A00001].
02:51	Player 2 - Maru (Terran) - Unit died KD8Charge [4200004].
02:55	Player 2 - Maru (Terran) - Unit born MULE [4200006]
02:55	Player 2 - Maru (Terran) - Unit initiated SupplyDepot [4240004]
02:57	Player 1 - Oliveira (Terran) - Unit born MULE [3E40002]
02:57	Player 1 - Oliveira (Terran) - Unit born SCV [4280002]
02:57	Player 2 - Maru (Terran) - Unit died MULE [3E40001].
02:59	Player 1 - Oliveira (Terran) - Unit died MULE [3E80001].
03:01	Player 1 - Oliveira (Terran) - Unit initiated SupplyDepotLowered [3E80002]
03:01	Player 2 - Maru (Terran) - Unit SupplyDepot [3900001] type changed to SupplyDepotLowered
03:02	Player 2 - Maru (Terran) - Unit born SCV [42C0002]
03:08	Player 1 - Oliveira (Terran) - Unit born Reaper [4300002]
03:09	Player 1 - Oliveira (Terran) - Unit born SCV [4340002]
03:10	Player 2 - Maru (Terran) - Unit Factory [3980002] done
03:10	Player 1 - Oliveira (Terran) - Unit died SCV [3500001].
03:13	Player 1 - Oliveira (Terran) - Unit born Hellion [3500002]
03:15	Player 2 - Maru (Terran) - Unit born SCV [4380002]
03:16	Player 1 - Oliveira (Terran) - Unit born Reaper [43C0002]
03:16	Player 2 - Maru (Terran) - Unit born Reaper [4400001]
03:17	Player 2 - Maru (Terran) - Unit SupplyDepot [4240004] done
03:21	Player 2 - Maru (Terran) - Unit born Reaper [4440001]
03:21	Player 1 - Oliveira (Terran) - Unit born SCV [4480001]
03:22	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3E80002] done
03:22	Player 2 - Maru (Terran) - Unit born KD8Charge [44C0001]
03:22	Player 2 - Maru (Terran) - Unit born KD8Charge [4500002]
03:23	Player 1 - Oliveira (Terran) - Unit born KD8Charge [3440003]
03:23	Player 1 - Oliveira (Terran) - Unit died Reaper [4300002].
03:23	Player 2 - Maru (Terran) - Unit died Reaper [3440002].
03:23	Player 2 - Maru (Terran) - Unit died KD8Charge [44C0001].
03:24	Player 2 - Maru (Terran) - Unit died KD8Charge [4500002].
03:25	Player 2 - Maru (Terran) - Unit born KD8Charge [44C0002]
03:25	Player 1 - Oliveira (Terran) - Unit died KD8Charge [3440003].
03:26	Player 2 - Maru (Terran) - Unit died KD8Charge [44C0002].
03:27	Player 2 - Maru (Terran) - Unit born KD8Charge [4300006]
03:28	Player 2 - Maru (Terran) - Unit died KD8Charge [4300006].
03:28	Player 2 - Maru (Terran) - Unit initiated OrbitalCommand [4300007]
03:28	Player 2 - Maru (Terran) - SprayTerran upgrade completed
03:29	Player 2 - Maru (Terran) - Unit born SCV [44C0003]
03:29	Player 2 - Maru (Terran) - Unit born KD8Charge [4500004]
03:30	Player 2 - Maru (Terran) - Unit died KD8Charge [4500004].
03:34	Player 2 - Maru (Terran) - Unit born Hellion [3440007]
03:35	Player 1 - Oliveira (Terran) - Unit born Hellion [4540004]
03:35	Player 2 - Maru (Terran) - Unit initiated FactoryTechLab [4500005]
03:40	Player 1 - Oliveira (Terran) - Unit born Reaper [4580002]
03:42	Player 1 - Oliveira (Terran) - Unit initiated Starport [45C0001]
03:42	Player 2 - Maru (Terran) - Unit initiated Starport [4600001]
03:43	Player 1 - Oliveira (Terran) - Unit born SCV [4640001]
03:44	Player 1 - Oliveira (Terran) - Unit OrbitalCommand [4080003] done
03:44	Player 2 - Maru (Terran) - Unit born SCV [4680001]
03:44	Player 1 - Oliveira (Terran) - SprayTerran upgrade completed
03:49	Player 2 - Maru (Terran) - Unit born Reaper [46C0002]
03:50	Player 1 - Oliveira (Terran) - Unit born Reaper [4700001]
03:51	Player 2 - Maru (Terran) - Unit BarracksFlying [3A40001] type changed to BarracksFlying
03:52	Player 2 - Maru (Terran) - Unit FactoryTechLab [4500005] done
03:53	Player 2 - Maru (Terran) - Unit born Reaper [4740001]
03:53	Player 2 - Maru (Terran) - Unit Barracks [3B80001] type changed to BarracksFlying
03:56	Player 2 - Maru (Terran) - Unit born SCV [4780002]
03:57	Player 1 - Oliveira (Terran) - Unit born SCV [47C0001]
03:58	Player 2 - Maru (Terran) - Unit initiated SupplyDepot [4800001]
03:59	Player 2 - Maru (Terran) - Unit born MULE [4840001]
04:00	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3D80001] type changed to SupplyDepot
04:01	Player 1 - Oliveira (Terran) - Unit SupplyDepot [3940001] type changed to SupplyDepot
04:02	Player 2 - Maru (Terran) - Unit died MULE [4200006].
04:03	Player 1 - Oliveira (Terran) - Unit born Hellion [4200007]
04:04	Player 1 - Oliveira (Terran) - Unit died MULE [3E40002].
04:06	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3D80001] type changed to SupplyDepotLowered
04:07	Player 1 - Oliveira (Terran) - Unit initiated FactoryTechLab [3E40003]
04:08	Player 2 - Maru (Terran) - Unit born SCV [4980001]
04:09	Player 2 - Maru (Terran) - Unit died Hellion [3440007].
04:10	Player 1 - Oliveira (Terran) - Unit born SCV [3440008]
04:10	Player 1 - Oliveira (Terran) - Unit born MULE [4A00001]
04:12	Player 1 - Oliveira (Terran) - Unit born Marine [49C0003]
04:12	Player 1 - Oliveira (Terran) - Unit born Marine [48C0003]
04:13	Player 1 - Oliveira (Terran) - Unit OrbitalCommand [4080003] type changed to OrbitalCommand
04:17	Player 1 - Oliveira (Terran) - Unit born MULE [4880003]
04:18	Player 1 - Oliveira (Terran) - Unit Starport [45C0001] done
04:18	Player 2 - Maru (Terran) - Unit Starport [4600001] done
04:20	Player 2 - Maru (Terran) - Unit SupplyDepot [4800001] done
04:21	Player 2 - Maru (Terran) - Unit born SCV [4940003]
04:22	Player 1 - Oliveira (Terran) - Unit born SCV [4900003]
04:25	Player 1 - Oliveira (Terran) - Unit FactoryTechLab [3E40003] done
04:26	Player 2 - Maru (Terran) - Unit born Cyclone [4A40001]
04:29	Player 1 - Oliveira (Terran) - Unit born SCV [4A80001]
04:32	Player 2 - Maru (Terran) - Unit initiated SupplyDepot [4AC0001]
04:34	Player 2 - Maru (Terran) - Unit born SCV [4B00001]
04:34	Player 1 - Oliveira (Terran) - Unit born SCV [4B40001]
04:36	Player 1 - Oliveira (Terran) - Unit born Marine [4B80001]
04:36	Player 1 - Oliveira (Terran) - Unit born Marine [4BC0001]
04:36	Player 1 - Oliveira (Terran) - Unit initiated SupplyDepot [4C00001]
04:40	Player 2 - Maru (Terran) - Unit OrbitalCommand [4300007] done
04:40	Player 2 - Maru (Terran) - SprayTerran upgrade completed
04:45	Player 2 - Maru (Terran) - Unit born SCV [4C40001]
04:46	Player 1 - Oliveira (Terran) - Unit born SCV [4C80001]
04:50	Player 2 - Maru (Terran) - Unit born Medivac [4CC0001]
04:51	Player 1 - Oliveira (Terran) - Unit born SCV [4D40001]
04:51	Player 2 - Maru (Terran) - Unit initiated StarportTechLab [4D00001]
04:53	Player 1 - Oliveira (Terran) - Unit initiated Refinery [4D80001]
04:54	Player 2 - Maru (Terran) - Unit SupplyDepot [4AC0001] done
04:54	Player 1 - Oliveira (Terran) - Unit SupplyDepotLowered [3E80002] type changed to SupplyDepotLowered
04:55	Player 2 - Maru (Terran) - Unit SupplyDepot [4AC0001] type changed to SupplyDepotLowered
04:57	Player 1 - Oliveira (Terran) - Unit SupplyDepot [4C00001] done
04:57	Player 2 - Maru (Terran) - Unit born SCV [4E00001]
04:57	Player 2 - Maru (Terran) - Unit initiated CommandCenter [4DC0001]
04:57	Player 2 - Maru (Terran) - Unit SupplyDepot [4AC0001] type changed to SupplyDepot
04:57	Player 2 - Maru (Terran) - SprayTerran upgrade completed
04:58	Player 1 - Oliveira (Terran) - Unit born SiegeTankSieged [4E40001]
04:59	Player 1 - Oliveira (Terran) - Unit born SCV [4E80001]
05:00	Player 2 - Maru (Terran) - Unit born Cyclone [4EC0001]
05:00	Player 1 - Oliveira (Terran) - Unit born Marine [4F00001]
05:01	Player 1 - Oliveira (Terran) - Unit born Medivac [4F40001]
05:01	Player 1 - Oliveira (Terran) - Unit born Marine [4F80001]
05:03	Player 1 - Oliveira (Terran) - Unit born SCV [4FC0001]
05:03	Player 1 - Oliveira (Terran) - Unit initiated StarportTechLab [5000001]
05:05	Player 2 - Maru (Terran) - Unit OrbitalCommand [4300007] type changed to OrbitalCommand
05:06	Player 2 - Maru (Terran) - Unit died MULE [4840001].
05:09	Player 2 - Maru (Terran) - Unit StarportTechLab [4D00001] done
05:09	Player 1 - Oliveira (Terran) - Unit born MULE [4840002]
05:10	Player 2 - Maru (Terran) - Unit born SCV [5040001]
05:11	Player 1 - Oliveira (Terran) - Unit born SCV [5080001]
05:12	Player 1 - Oliveira (Terran) - Unit initiated SupplyDepot [50C0001]
05:15	Player 1 - Oliveira (Terran) - Unit Refinery [4D80001] done
05:15	Player 1 - Oliveira (Terran) - Unit born SCV [5100001]
05:18	Player 1 - Oliveira (Terran) - Unit died MULE [4A00001].
05:20	Player 2 - Maru (Terran) - Unit born SCV [4A00002]
05:21	Player 1 - Oliveira (Terran) - Unit StarportTechLab [5000001] done
05:22	Player 1 - Oliveira (Terran) - Unit born MULE [5140001]
05:22	Player 1 - Oliveira (Terran) - Unit born Marine [5180001]
05:22	Player 2 - Maru (Terran) - Unit Barracks [3B80001] type changed to Barracks
05:23	Player 1 - Oliveira (Terran) - Unit born SCV [51C0001]
05:23	Player 2 - Maru (Terran) - Unit born SCV [5200001]
05:25	Player 1 - Oliveira (Terran) - Unit died MULE [4880003].
05:26	Player 2 - Maru (Terran) - Unit died SCV [42C0002].
05:29	Player 1 - Oliveira (Terran) - Unit born SCV [42C0003]
05:29	Player 2 - Maru (Terran) - Unit OrbitalCommand [4300007] type changed to OrbitalCommandFlying
05:30	Player 1 - Oliveira (Terran) - Unit born Cyclone [4880004]
05:32	Player 1 - Oliveira (Terran) - Unit born Marine [3D40002]
05:32	Player 1 - Oliveira (Terran) - Unit died SCV [3D40001].
05:33	Player 1 - Oliveira (Terran) - Unit SupplyDepot [50C0001] done
05:33	Player 2 - Maru (Terran) - Unit died SCV [3680001].
05:33	Player 2 - Maru (Terran) - Unit died SCV [3A00002].
05:34	Player 2 - Maru (Terran) - Unit died SCV [5200001].
05:35	Player 2 - Maru (Terran) - Unit born SiegeTankSieged [3A00003]
05:35	Player 2 - Maru (Terran) - Unit born SCV [3400002]
05:35	Player 1 - Oliveira (Terran) - Unit died SCV [4280002].
05:35	Player 1 - Oliveira (Terran) - Unit died SCV [3400001].
05:35	Player 1 - Oliveira (Terran) - Unit died SCV [3480001].
05:35	Player 2 - Maru (Terran) - Unit SupplyDepot [3900001] type changed to SupplyDepot
05:36	Player 2 - Maru (Terran) - Unit died SCV [4A00002].
05:36	Player 2 - Maru (Terran) - Unit died SCV [40C0001].
05:37	Player 1 - Oliveira (Terran) - Unit died Hellion [41C0003].
05:37	Player 2 - Maru (Terran) - Unit died SCV [4940003].
05:37	Player 1 - Oliveira (Terran) - Unit died Hellion [3500002].
05:37	Player 2 - Maru (Terran) - Unit died SCV [4B00001].
05:38	Player 2 - Maru (Terran) - Unit died SCV [4E00001].
05:38	Player 1 - Oliveira (Terran) - Unit died SCV [3340001].
05:38	Player 2 - Maru (Terran) - Unit died Reaper [46C0002].
05:38	Player 2 - Maru (Terran) - Unit died SCV [5040001].
05:39	Player 1 - Oliveira (Terran) - Unit died SCV [3B40001].
05:39	Player 2 - Maru (Terran) - Unit died SCV [44C0003].
05:40	Player 1 - Oliveira (Terran) - Unit died SCV [34C0001].
05:40	Player 1 - Oliveira (Terran) - Unit died SCV [4480001].
05:40	Player 1 - Oliveira (Terran) - Unit SiegeTankSieged [4E40001] type changed to SiegeTankSieged
05:40	Player 2 - Maru (Terran) - Unit SiegeTankSieged [3A00003] type changed to SiegeTankSieged
05:42	Player 2 - Maru (Terran) - Unit born Marine [4100002]
05:42	Player 1 - Oliveira (Terran) - Unit died SCV [4100001].
05:42	Player 2 - Maru (Terran) - Unit died SCV [3400002].
05:42	Player 1 - Oliveira (Terran) - Unit died SCV [4040001].
05:43	Player 1 - Oliveira (Terran) - Unit died SCV [4640001].
05:43	Player 1 - Oliveira (Terran) - Unit died SCV [32C0001].
05:44	Player 1 - Oliveira (Terran) - Unit born SCV [3F80003]
05:44	Player 1 - Oliveira (Terran) - Unit died Hellion [4540004].
05:44	Player 1 - Oliveira (Terran) - Unit died Reaper [3F80002].
05:44	Player 1 - Oliveira (Terran) - Unit died SCV [3240001].
05:45	Player 1 - Oliveira (Terran) - Unit born SCV [43C0003]
05:45	Player 2 - Maru (Terran) - Unit died SiegeTankSieged [3A00003].
05:45	Player 1 - Oliveira (Terran) - Unit died Reaper [43C0002].
05:45	Player 2 - Maru (Terran) - Unit died Marine [4100002].
05:47	Player 2 - Maru (Terran) - Unit born SCV [4400002]
05:47	Player 2 - Maru (Terran) - Unit died Reaper [4400001].
05:48	Player 1 - Oliveira (Terran) - Unit died SCV [42C0003].
05:48	Player 2 - Maru (Terran) - Unit died BarracksFlying [3A40001].
05:49	Player 2 - Maru (Terran) - Unit died Reaper [33C0002].
05:50	Player 1 - Oliveira (Terran) - Unit died Cyclone [4880004].
05:51	Player 1 - Oliveira (Terran) - Unit born Marine [4400003]
05:51	Player 1 - Oliveira (Terran) - Unit born Marine [4880005]
05:51	Player 2 - Maru (Terran) - Unit died SCV [4400002].
05:52	Player 2 - Maru (Terran) - Unit died Reaper [4740001].
05:53	Player 2 - Maru (Terran) - Unit died Reaper [4440001].
05:53	Player 2 - Maru (Terran) - Unit died FactoryTechLab [4500005].
05:53	Player 1 - Oliveira (Terran) - Unit SiegeTankSieged [4E40001] type changed to SiegeTank
05:56	Player 2 - Maru (Terran) - Unit born Banshee [4500006]
05:58	Player 2 - Maru (Terran) - Unit OrbitalCommand [4300007] type changed to OrbitalCommand
05:58	Player 1 - Oliveira (Terran) - Unit SiegeTankSieged [4E40001] type changed to SiegeTankSieged
06:00	Player 2 - Maru (Terran) - Unit born SCV [4740004]
06:00	Player 2 - Maru (Terran) - Unit born Marine [4440005]
06:00	Player 2 - Maru (Terran) - Unit died Reaper [4000001].
06:01	Player 1 - Oliveira (Terran) - Unit born SCV [4000002]
06:01	Player 2 - Maru (Terran) - Unit born MULE [4440006]
06:01	Player 2 - Maru (Terran) - Unit died Marine [4440005].
06:01	Player 2 - Maru (Terran) - Unit died SCV [3740001].
06:02	Player 2 - Maru (Terran) - Unit born MULE [3740002]
06:02	Player 2 - Maru (Terran) - Unit died SCV [4740004].
06:02	Player 2 - Maru (Terran) - Unit died Reaper [3F00001].
06:04	Player 1 - Oliveira (Terran) - Unit born SCV [3F00002]
06:06	Player 2 - Maru (Terran) - Unit died Medivac [4CC0001].
06:07	Player 1 - Oliveira (Terran) - Unit born Raven [4CC0002]
06:08	Player 2 - Maru (Terran) - Unit CommandCenter [4DC0001] done
06:08	Player 1 - Oliveira (Terran) - Unit born MULE [4740005]
06:08	Player 2 - Maru (Terran) - SprayTerran upgrade completed
06:09	Player 1 - Oliveira (Terran) - Unit born Marine [4D00002]
06:09	Player 1 - Oliveira (Terran) - Unit born Marine [33C0006]
06:09	Player 2 - Maru (Terran) - Unit died StarportTechLab [4D00001].
06:10	Player 2 - Maru (Terran) - Unit born SCV [410000A]
06:12	Player 2 - Maru (Terran) - Unit born SCV [3A40004]
06:12	Player 1 - Oliveira (Terran) - Unit born SiegeTank [3900002]
06:12	Player 2 - Maru (Terran) - Unit died SupplyDepot [3900001].
06:13	Player 1 - Oliveira (Terran) - Unit born SCV [42C0007]
06:16	Player 1 - Oliveira (Terran) - Unit born SCV [32C0007]
06:16	Player 1 - Oliveira (Terran) - Unit died MULE [4840002].
06:22	Player 2 - Maru (Terran) - Unit born SCV [3240006]
06:22	Player 2 - Maru (Terran) - Unit died Cyclone [4A40001].
06:24	Player 2 - Maru (Terran) - Unit died Cyclone [4EC0001].
06:25	Player 1 - Oliveira (Terran) - Unit born SCV [4EC0003]
06:27	Player 1 - Oliveira (Terran) - Unit born Marine [4A40005]
06:27	Player 1 - Oliveira (Terran) - Unit born Marine [4840004]
06:27	Player 2 - Maru (Terran) - Unit died SCV [4380002].
06:29	Player 1 - Oliveira (Terran) - Unit born SCV [4380003]
06:29	Player 1 - Oliveira (Terran) - Unit died MULE [5140001].
        """,
        },
    ],
)
print(response.choices[0].message.content)
