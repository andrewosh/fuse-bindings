{
  'variables': {
    'target_arch%': '<!(node preinstall.js --print-arch)>'
  },
  'targets': [
    {
      'target_name': 'fuse',
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        'deps/libfuse/include'
      ],
      'sources': [
        'src/abstractions.cc',
        'src/fuse-bindings.cc',
      ],
      'libraries': [
        '<!(node preinstall.js --print-lib)'
      ],     
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-g',
          '-O3',
        ]
      },
      'cflags': [
        '-g',
        '-O3',
      ],

    }
  ]
}
