#include <cstdint>
#include <algorithm>
extern "C" int rref(int64_t* a, int rows, int cols, int prime, int* pivots) {
  int rank=0;
  for(int col=0; col<cols && rank<rows; ++col){
    int src=rank; while(src<rows && a[(int64_t)src*cols+col]==0) ++src;
    if(src==rows) continue;
    if(src!=rank) for(int j=col;j<cols;++j) std::swap(a[(int64_t)src*cols+j],a[(int64_t)rank*cols+j]);
    int64_t* p=a+(int64_t)rank*cols;
    int64_t inv=1,base=p[col]; int exp=prime-2;
    while(exp){if(exp&1) inv=inv*base%prime; base=base*base%prime; exp>>=1;}
    for(int j=col;j<cols;++j) p[j]=p[j]*inv%prime;
    for(int i=0;i<rows;++i) if(i!=rank){
      int64_t* q=a+(int64_t)i*cols; int64_t factor=q[col];
      if(!factor) continue;
      for(int j=col+1;j<cols;++j) {int64_t v=(q[j]-factor*p[j])%prime; q[j]=v<0?v+prime:v;}
      q[col]=0;
    }
    pivots[rank++]=col;
  }
  return rank;
}
