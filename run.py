import argparse
import multiprocessing
from process_app import process_1, process_2, process_3
if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("--video_src", type=int, default= 1,help="Source camera")
    args = ap.parse_args()

    p1 = multiprocessing.Process(target=process_1, args=(args.video_src, ))
    p2 = multiprocessing.Process(target=process_2, args=())
    p3 = multiprocessing.Process(target=process_3, args=())
  
    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    #start process 3
    p3.start()
  
    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # wait until process 2 is finished
    p3.join()

    

   
